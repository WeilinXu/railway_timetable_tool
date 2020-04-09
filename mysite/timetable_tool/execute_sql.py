from django.db import connection, transaction
import datetime
from timetable_tool.models import tickets

def query_db(query, args=(), one=False, commit=False):
    cursor = connection.cursor()
    cur = cursor.execute(query, args)
    columns = [col[0] for col in cur.description]
    if(commit):
        transaction.commit_unless_managed()
    if one:
        rv = [dict(zip(columns, row)) for row in cur.fetchone()]
    else:
        rv = [dict(zip(columns, row)) for row in cur.fetchall()]
    return rv

def replace_from_dash(route_num):
    return route_num.replace('/','-')

def replace_to_dash(route_num):
    return route_num.replace('-','/')

# TODO: remove magic numbers: railwayhistory.app.config['MAX_STATION_LENGTH']
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
    route_query = "SELECT S.id AS station_id, S.station_name AS station_name, " \
                        + "T.id AS train_record_id, TR.station_no AS station_no, " \
                        + "TR.arr_time AS arr_time, TR.arr_day AS arr_day, " \
                        + "TR.dep_time AS dep_time " \
                    + "FROM timetable_tool_stations S, timetable_tool_train_records T, timetable_tool_stop_records TR " \
                    + "WHERE T.id = TR.train_record_id AND S.id = TR.station_id "\
                        + "AND T.train_number = %s "  \
                    + " ORDER BY station_no" 
    route_result = query_db(route_query, args = [route_in])
    return route_result



def get_station_query(station_in, date_in):
    station_query = "SELECT S.id AS station_id, S.station_name AS station_name," \
                        + "T.id AS train_record_id, T.train_number as train_number," \
                    + "S1.station_name AS station_from, S2.station_name AS station_to, " \
                    + "TR.arr_time AS arr_time, " \
                    + "TR.dep_time AS dep_time " \
                    + "FROM timetable_tool_stations S, timetable_tool_train_records T, " \
                    + "timetable_tool_stop_records TR, timetable_tool_stations S1, timetable_tool_stations S2 " \
                    + "WHERE S.station_name = %s " \
                        + "AND S.id = TR.station_id AND T.id = TR.train_record_id " \
                    +"AND T.train_from_id = S1.id AND T.train_to_id = S2.id " \
                    + "ORDER BY T.train_number"
    station_results = query_db(station_query, args = [station_in])
    for station_result in station_results:
        station_result["train_link"] = replace_from_dash(station_result["train_number"])
    return station_results

# [station_depart, station_dest, station_depart_id, station_dest_id, train_record_id, station_to
#  station_from, station_to, dep_time, dep_day, arr_time, arr_day, TRto_id, TRfrom_id,
# train_link, day_str, time_delta]
def get_train_query(depart_in, dest_in, date_in):
    train_query = "SELECT Sfrom.station_name AS station_depart, Sto.station_name AS station_dest," \
                        + "Sfrom.id AS station_depart_id, Sto.id AS station_dest_id," \
                        + "T.id AS train_record_id, T.train_number AS train_number," \
                        + "S1.station_name AS station_from, S2.station_name AS station_to, " \
                        + "TRfrom.dep_time AS dep_time, TRfrom.dep_day AS dep_day, " \
                        + "TRto.arr_time AS arr_time, TRto.arr_day AS arr_day, " \
                        + "TRto.id AS TRto_id, TRfrom.id AS TRfrom_id " \
                    + "FROM timetable_tool_stations Sfrom, timetable_tool_stations Sto, timetable_tool_stop_records TRfrom, " \
                        + "timetable_tool_stop_records TRto, timetable_tool_train_records T, " \
                        + "timetable_tool_stations S1, timetable_tool_stations S2 " \
                    + "WHERE Sfrom.station_name = %s " \
                        + "AND Sto.station_name = %s " \
                        + "AND Sfrom.id = TRfrom.station_id AND Sto.id = TRto.station_id " \
                        + "AND TRfrom.station_no < TRto.station_no AND TRfrom.train_record_id = TRto.train_record_id " \
                        + "AND TRfrom.train_record_id = T.id " \
                        + "AND T.train_from_id = S1.id AND T.train_to_id = S2.id " \
                    + "ORDER BY T.train_number"
    train_results = query_db(train_query, [depart_in, dest_in])
    for train_result in train_results:
        train_result["train_link"] = replace_from_dash(train_result["train_number"])
        delta_day = train_result["arr_day"] - train_result["dep_day"]
        if(delta_day == 0):
            train_result["day_str"] = ""
        elif(delta_day == 1):
            train_result["day_str"] = "On 2nd day"
        elif(delta_day == 2):
            train_result["day_str"] = "On 3rd day"
        else:
            train_result["day_str"] = "On " + str(delta_day) + "th day"
        cur_day = datetime.datetime.strptime(date_in, '%Y-%m-%d')
        t2 = datetime.datetime.combine(cur_day + datetime.timedelta(days = delta_day), train_result["arr_time"])
        t1 = datetime.datetime.combine(cur_day, train_result["dep_time"])
        train_result['time_delta'] = t2 - t1 
        # seat avaliable search
        if tickets.objects.filter(stop_from_id = train_result["TRfrom_id"], \
                stop_to_id = train_result["TRto_id"], train_date = date_in): 
            tickets_all = tickets.objects.get(stop_from_id = train_result["TRfrom_id"], \
                stop_to_id = train_result["TRto_id"], train_date = date_in)
            train_result["seats_avaliable"] = tickets_all.tickets_avaliable
        else:
            train_result["seats_avaliable"] = 0
    return train_results



def get_ticket_bought(user_id_in):
    ticket_query = "SELECT TKS.id AS ticket_id, TK.train_date AS train_date, " \
                    + "TRfrom.dep_time AS dep_time, TRfrom.dep_day AS dep_day, "\
                    + "TRto.arr_time AS arr_time, TRto.arr_day AS arr_day, " \
                    + "S1.station_name AS station_from, S2.station_name AS station_to, "\
                    + "T.train_number AS train_number "\
                    + "FROM timetable_tool_tickets_sold AS TKS, timetable_tool_tickets AS TK, "\
                    + "timetable_tool_stop_records AS TRfrom, timetable_tool_stop_records AS TRto, "\
                    + "timetable_tool_stations S1, timetable_tool_stations S2, "\
                    + "timetable_tool_train_records T " \
                    + "WHERE TKS.customer_id = {} AND TKS.ticket_id = TK.id "\
                    + "AND TK.stop_from_id = TRfrom.id AND TK.stop_to_id = TRto.id "\
                    + "AND TRfrom.station_id = S1.id AND TRto.station_id = S2.id "\
                    + "AND TRfrom.train_record_id = T.id " \
                    + "ORDER BY TK.train_date DESC"
    ticket_results = query_db(ticket_query.format(user_id_in), [])
    for ticket_result in ticket_results:
        delta_day = ticket_result["arr_day"] - ticket_result["dep_day"]
        cur_day = ticket_result["train_date"]
        ticket_result["train_link"] = replace_from_dash(ticket_result["train_number"])
        ticket_result["train_date_str"] = str(ticket_result["train_date"])
        ticket_result["dep_datetime"] = datetime.datetime.combine(cur_day, ticket_result["dep_time"])
        ticket_result["arr_datetime"] = datetime.datetime.combine(cur_day + datetime.timedelta(days = delta_day), ticket_result["arr_time"])
        
    return ticket_results