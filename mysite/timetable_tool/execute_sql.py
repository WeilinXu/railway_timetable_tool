from django.db import connection, transaction
import datetime

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
   
# TODO: date
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

def get_train_query(depart_in, dest_in, date_in):
    train_query = "SELECT Sfrom.station_name AS station_depart, Sto.station_name AS station_dest," \
                        + "Sfrom.id AS station_depart_id, Sto.id AS station_dest_id," \
                        + "T.id AS train_record_id, T.train_number AS train_number," \
                        + "S1.station_name AS station_from, S2.station_name AS station_to, " \
                        + "TRfrom.dep_time AS dep_time, TRfrom.dep_day AS dep_day, " \
                        + "TRto.arr_time AS arr_time, TRto.arr_day AS arr_day " \
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
    return train_results