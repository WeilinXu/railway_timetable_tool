from django.db import connection, transaction
import datetime

def query_db(query, args=(), one=False, commit=False):
    cursor = connection.cursor()
    cur = cursor.execute(query, args)
    if(commit):
        transaction.commit_unless_managed()
    if one:
        rv = cur.fetchone()
    else:
        rv = cur.fetchall()
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
                        + "T.id AS train_record_id, TR.station_no AS station_no " \
                    + "FROM timetable_tool_stations S, timetable_tool_train_records T, timetable_tool_stop_records TR " \
                    + "WHERE T.id = TR.id AND S.id = TR.id "\
                        + "AND T.train_number = %s "  \
                    + " ORDER BY station_no" 
    route_result = query_db(route_query, args = [route_in])
    return route_result



def get_station_query(station_in, date_in):
    station_query = "SELECT S.id AS station_id, S.station_name AS station_name," \
                        + "T.id AS train_record_id, T.train_number as train_number," \
                    + "S1.station_name AS station_from, S2.station_name AS station_to " \
                    + "FROM timetable_tool_stations S, timetable_tool_train_records T, " \
                    + "timetable_tool_stop_records TR, timetable_tool_stations S1, timetable_tool_stations S2 " \
                    + "WHERE S.station_name = %s " \
                        + "AND S.id = TR.id AND T.id = TR.id " \
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
                        + "S1.station_name AS station_from, S2.station_name AS station_to " \
                    + "FROM timetable_tool_stations Sfrom, timetable_tool_stations Sto, timetable_tool_stop_records TRfrom, " \
                        + "timetable_tool_stop_records TRto, timetable_tool_train_records T, " \
                        + "timetable_tool_stations S1, timetable_tool_stations S2 " \
                    + "WHERE Sfrom.station_name = %s " \
                        + "AND Sto.station_name = %s " \
                        + "AND Sfrom.id = TRfrom.id AND Sto.id = TRto.id " \
                        + "AND TRfrom.station_no < TRto.station_no AND TRfrom.id = TRto.id " \
                        + "AND TRfrom.id = T.id " \
                        + "AND T.train_from_id = S1.id AND T.train_to_id = S2.id " \
                    + "ORDER BY T.train_number"
    train_results = query_db(train_query, [depart_in, dest_in])
    for train_result in train_results:
        train_result["train_link"] = replace_from_dash(train_result["train_number"])
    return train_results