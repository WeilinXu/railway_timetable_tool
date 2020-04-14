from django.db import connection, transaction
import datetime
from timetable_tool.models import tickets, stations, train_records, stop_records
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

def query_db(query, args=(), one=False, commit=False):
    cursor = connection.cursor()
    cur = cursor.execute(query, args)
    columns = [col[0] for col in cur.description]
    if one:
        rv = [dict(zip(columns, row)) for row in cur.fetchone()]
    else:
        rv = [dict(zip(columns, row)) for row in cur.fetchall()]
    return rv

def replace_from_dash(route_num):
    return route_num.replace('/','-')

def replace_to_dash(route_num):
    return route_num.replace('-','/')

def valid_station(station_in):
    return (station_in and len(station_in) <= 20)

def valid_route(route_in):
    return (route_in and len(route_in) <= 20)

def valid_date(date_in):
    try:
        datetime.datetime.strptime(date_in, '%Y-%m-%d')
    except ValueError:
        return False
    return True
   

def get_route_query(route_in, date_in):
    route_in_real = train_records.objects.filter(train_number = route_in)
    if(not route_in_real):
        route_in1 = route_in + '/'
        route_in2 = '/' + route_in
        route_in_real = train_records.objects.filter(Q(train_number__contains = route_in1)| \
                        Q(train_number__contains = route_in2))
        if(not route_in_real):
            return {}
    route_in_real = route_in_real[0].train_number
    print(route_in_real)

    route_query = "SELECT S.id AS station_id, S.station_name AS station_name, " \
                        + "S.station_name_cn AS station_name_cn, " \
                        + "T.id AS train_record_id, TR.station_no AS station_no, " \
                        + "TR.arr_time AS arr_time, TR.arr_day AS arr_day, " \
                        + "TR.dep_time AS dep_time, TR.km AS km " \
                    + "FROM timetable_tool_stations S, timetable_tool_train_records T, timetable_tool_stop_records TR " \
                    + "WHERE T.id = TR.train_record_id AND S.id = TR.station_id "\
                        + "AND T.train_number = %s "  \
                    + " ORDER BY station_no" 
    
    route_results = query_db(route_query, args = [route_in_real])
    for route_result in route_results:
        route_result["arr_day"] = route_result["arr_day"] + 1
    return route_results



def get_station_query(station_in, date_in):
    query1 = "SELECT S.id AS station_id, S.station_name AS station_name," \
                    + "S.station_name_cn AS station_name_cn," \
                        + "T.id AS train_record_id, T.train_number as train_number," \
                    + "S1.station_name AS station_from, S2.station_name AS station_to, " \
                    + "S1.station_name_cn AS station_from_cn, S2.station_name_cn AS station_to_cn, " \
                    + "TR.arr_time AS arr_time, " \
                    + "TR.dep_time AS dep_time " \
                    + "FROM timetable_tool_stations S, timetable_tool_train_records T, " \
                    + "timetable_tool_stop_records TR, timetable_tool_stations S1, timetable_tool_stations S2 "
    query3 = "AND S.id = TR.station_id AND T.id = TR.train_record_id " \
                    +"AND T.train_from_id = S1.id AND T.train_to_id = S2.id " \
                    + "ORDER BY T.train_number"
    if(is_cn()):
        station_query = query1 + "WHERE S.station_name_cn = %s " + query3
    else:
        station_query = query1 + "WHERE S.station_name = %s " + query3
    station_results = query_db(station_query, args = [station_in])
    for station_result in station_results:
        station_result["train_link"] = replace_from_dash(station_result["train_number"])
    return station_results

# [station_depart, station_dest, station_depart_id, station_dest_id, train_record_id, station_to
#  station_from, station_to, dep_time, dep_day, arr_time, arr_day, TRto_id, TRfrom_id,
# train_link, day_str, time_delta]
def get_train_query(depart_in, dest_in, date_in): 
    q_is_cn = is_cn()
    if(q_is_cn):
        group_from = stations.objects.filter(station_name_cn = depart_in)
        group_to = stations.objects.filter(station_name_cn = dest_in)
    else:
        group_from = stations.objects.filter(station_name = depart_in)
        group_to = stations.objects.filter(station_name = dest_in)
    
    if(not group_from or not group_to):
        return {}
    q1 = "SELECT Sfrom.station_name AS station_depart, Sto.station_name AS station_dest, " \
            + "Sfrom.station_name_cn AS station_depart_cn, Sto.station_name_cn AS station_dest_cn, "\
            + "Sfrom.id AS station_depart_id, Sto.id AS station_dest_id, " \
            + "T.id AS train_record_id, T.train_number AS train_number, " \
            + "TRfrom.dep_time AS dep_time, TRfrom.dep_day AS dep_day, " \
            + "TRto.arr_time AS arr_time, TRto.arr_day AS arr_day, " \
            + "TRfrom.km AS km_from, TRto.km AS km_to, "\
            + "TRto.id AS TRto_id, TRfrom.id AS TRfrom_id " \
        + "FROM timetable_tool_stations Sfrom, timetable_tool_stations Sto, timetable_tool_stop_records TRfrom, " \
            + "timetable_tool_stop_records TRto, timetable_tool_train_records T "
    if(group_from[0].group_city_id == group_to[0].group_city_id):   # corner case
        if(q_is_cn):
            q2 = "WHERE Sfrom.station_name_cn = %s AND Sto.station_name_cn = %s "
        else:
            q2 = "WHERE Sfrom.station_name = %s AND Sto.station_name = %s "
        
        q3 = "AND Sfrom.id = TRfrom.station_id AND Sto.id = TRto.station_id " \
                + "AND TRfrom.station_no < TRto.station_no AND TRfrom.train_record_id = TRto.train_record_id " \
                + "AND TRfrom.train_record_id = T.id " \
            + "ORDER BY T.train_number"
        train_query = q1 + q2 + q3
        train_results = query_db(train_query , [depart_in, dest_in])
    else:
        q2 = "WHERE Sfrom.group_city_id = {} " \
                            + "AND Sto.group_city_id = {} " \
                            + "AND Sfrom.id = TRfrom.station_id AND Sto.id = TRto.station_id " \
                            + "AND TRfrom.station_no < TRto.station_no AND TRfrom.train_record_id = TRto.train_record_id " \
                            + "AND TRfrom.train_record_id = T.id " \
                        + "ORDER BY T.train_number, Sfrom.station_name, Sto.station_name"
        train_query = q1 + q2
        train_results = query_db(train_query.format(group_from[0].group_city_id, group_to[0].group_city_id), [])
        # remove duplicated results
        idx_keep = []
        for idx in range(len(train_results)):
            if(len(idx_keep) is 0 or train_results[idx]["train_record_id"] is not \
                    train_results[idx_keep[-1]]["train_record_id"]):
                idx_keep.append(idx)
                is_dep = (train_results[idx]["station_depart"] == depart_in)
                is_arr = (train_results[idx]["station_dest"] == dest_in)
            elif(not is_dep or not is_arr):
                is_dep_cur = (train_results[idx]["station_depart"] == depart_in)
                is_arr_cur = (train_results[idx]["station_dest"] == dest_in)
                if((is_dep_cur and not is_dep) or (is_dep_cur and is_arr_cur and not is_arr)):
                    is_dep = is_dep_cur
                    is_arr = is_arr_cur
                    idx_keep[-1] = idx
        train_results = [ train_results[i] for i in idx_keep]
    
    cur_day = datetime.datetime.strptime(date_in, '%Y-%m-%d')
    for train_result in train_results:
        train_result["train_link"] = replace_from_dash(train_result["train_number"])
        arr_date, delta_day = get_arr_date(train_result["dep_day"], cur_day, train_result["arr_day"])
        if(delta_day == 0):
            train_result["day_str"] = ""
        elif(delta_day == 1):
            train_result["day_str"] = _("on 2nd day")
        elif(delta_day == 2):
            train_result["day_str"] = _("on 3rd day")
        else:
            train_result["day_str"] = _("on %(del)dth day") % {'del' : str(delta_day)}
        
        t2 = datetime.datetime.combine(arr_date, train_result["arr_time"])
        t1 = datetime.datetime.combine(cur_day, train_result["dep_time"])
        time_delta_raw = (t2 - t1).total_seconds()
        train_result['time_delta'] = _("%(hr_str)sh %(min_str)smin")% {'hr_str' : ("%02d" % ((time_delta_raw // 3600))), \
                    'min_str' : ("%02d" % ((time_delta_raw % 3600) // 60))}
        train_result['km_delta'] = train_result['km_to'] - train_result['km_from']
        train_result['price'] = get_price(train_result['km_delta'])
        # seat avaliable search
        if tickets.objects.filter(stop_from_id = train_result["TRfrom_id"], \
                stop_to_id = train_result["TRto_id"], train_date = date_in): 
            tickets_all = tickets.objects.get(stop_from_id = train_result["TRfrom_id"], \
                stop_to_id = train_result["TRto_id"], train_date = date_in)
            train_result["seats_avaliable"] = tickets_all.tickets_avaliable
        else:
            train_result["seats_avaliable"] = 0
        train_result['can_buy'] = (t1 > datetime.datetime.now())

    return train_results



def get_ticket_bought(user_id_in, mode = 'future'):
    datetime_now = datetime.datetime.now()
    date_now = datetime_now.strftime("%Y-%m-%d")
    clock_now = datetime_now.strftime("%H:%M")
    q1 = "SELECT TKS.id AS ticket_id, TK.train_date AS train_date, " \
                    + "TKS.seat_number AS seat_number, "\
                    + "TKS.quantity AS quantity, TKS.price AS price, "\
                    + "TRfrom.dep_time AS dep_time, TRfrom.dep_day AS dep_day, "\
                    + "TRto.arr_time AS arr_time, TRto.arr_day AS arr_day, " \
                    + "S1.station_name AS station_from, S2.station_name AS station_to, "\
                    + "S1.station_name AS station_from_cn, S2.station_name AS station_to_cn, "\
                    + "T.train_number AS train_number "\
                    + "FROM timetable_tool_tickets_sold AS TKS, timetable_tool_tickets AS TK, "\
                    + "timetable_tool_stop_records AS TRfrom, timetable_tool_stop_records AS TRto, "\
                    + "timetable_tool_stations S1, timetable_tool_stations S2, "\
                    + "timetable_tool_train_records T " \
                    + "WHERE TKS.customer_id = {} AND TKS.ticket_id = TK.id "
    q3 = "AND TK.stop_from_id = TRfrom.id AND TK.stop_to_id = TRto.id "\
                    + "AND TRfrom.station_id = S1.id AND TRto.station_id = S2.id "\
                    + "AND TRfrom.train_record_id = T.id " \
                    + "ORDER BY TK.train_date "
    if(mode is 'future'):
        q2 = "AND (TK.train_date > %s "\
            + "OR (TK.train_date = %s AND TRfrom.dep_time > %s )) "
        ticket_query = q1 + q2 + q3
    else:
        q2 = "AND (TK.train_date < %s "\
            + "OR (TK.train_date = %s AND TRfrom.dep_time < %s )) "
        ticket_query = q1 + q2 + q3 + " DESC"
    
    ticket_results = query_db(ticket_query.format(user_id_in), [date_now, date_now, clock_now])  # 
    for ticket_result in ticket_results:
        cur_day = ticket_result["train_date"]
        arr_date, _ = get_arr_date(ticket_result["dep_day"], cur_day, ticket_result["arr_day"])
        ticket_result["train_link"] = replace_from_dash(ticket_result["train_number"])
        ticket_result["train_date_str"] = str(ticket_result["train_date"])
        ticket_result["dep_datetime"] = datetime.datetime.combine(cur_day, ticket_result["dep_time"])
        ticket_result["arr_datetime"] = datetime.datetime.combine(arr_date, ticket_result["arr_time"])
        
    return ticket_results

def get_stop_record_info(stop_record_id_in, is_arr = False):
    stop_record_obj = stop_records.objects.get(id =  stop_record_id_in)
    stop_info = {}
    if(is_arr):
        stop_info['stop_time'] = stop_record_obj.arr_time
        stop_info['stop_day'] = stop_record_obj.arr_day
    else:
        stop_info['stop_time'] = stop_record_obj.dep_time
        stop_info['stop_day'] = stop_record_obj.dep_day
    
    route_obj = train_records.objects.get(id =  stop_record_obj.train_record_id)
    station_obj = stations.objects.get(id =  stop_record_obj.station_id)
    stop_info['station_name'] = station_obj.station_name
    stop_info['station_name_cn'] = station_obj.station_name_cn
    stop_info['train_number'] = route_obj.train_number
    stop_info['km'] = stop_record_obj.km
    return stop_info

def get_arr_date(dep_day_in, dep_date_in, arr_day_in):
    delta_day =  arr_day_in - dep_day_in
    return dep_date_in + datetime.timedelta(days = delta_day), delta_day

def get_price(km_distance):
    return int(0.3 * km_distance)

def can_cancel(ticket_session_obj, idx):
    if str(idx) not in ticket_session_obj:
        return False
    ticket_date = datetime.datetime.strptime(ticket_session_obj[str(idx)]['depart_date'], '%Y-%m-%d')
    ticket_time = datetime.datetime.strptime(ticket_session_obj[str(idx)]['depart_time'],'%H:%M:%S').time()
    ticket_datetime = datetime.datetime.combine(ticket_date, ticket_time)
    return (ticket_datetime > datetime.datetime.now())
    

def is_cn():
    return get_language() == 'zh-hans'