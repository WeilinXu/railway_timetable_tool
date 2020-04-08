
import os
import re
import datetime 

'''
record sytle:
route_number1,route_number2 | start_date | end_date | 
        stop1/u(arrive_time/depart_time), ..., stopN | \n
add further: time, distance, comment
invariant to maintain: station_id, route_id, end_date
'''

## TODO: rename / update, history, multiple_train_num
## TODO: / to %2F in url
## TODO: mo hu search
## TODO: keep old search in form
## TODO: consider date
def get_station_sql(stop):
    s1 = "INSERT INTO timetable_tool_stations (station_name) " \
            + "VALUES ('{}');\n".format(stop)
    
    return s1

def get_route_sql(number, fromid, toid):
    s1 = "INSERT INTO timetable_tool_train_records (train_number"\
            + ", train_from_id, train_to_id"
    s2 = " VALUES ('{}', {}, {}".format(number, fromid, toid)
    s3 = s1 + ")" + s2 + ");\n"
    return s3

def get_stop_sql(tid, s_info, sno):
    s1 = "INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, "\
        + "arr_time, arr_day, dep_time, dep_day) " \
        + "VALUES ({}, {}, {}, '{}', {}, '{}', {});\n".format(tid, s_info[0], sno, s_info[1], s_info[3], s_info[2], s_info[4])
    return s1

def get_ticket_sql(tr_id1, tr_id2, ticket_date = '2020-05-05', tickets_avaliable = 5):
    s1 = "INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, "\
        + "tickets_avaliable) VALUES ({}, {}, '{}', {});\n".format(tr_id1, tr_id2, ticket_date, tickets_avaliable)
    return s1

def count_stations(filepath_read, filepath_write):
    station2id = {}
    f_read = open(filepath_read, 'r')
    f_write = open(filepath_write, 'w')
    lines_r = f_read.readlines()
    count = 1
    for line_r in lines_r:
        if line_r == '\n':
            continue
        item = line_r[:-1]  # remove last '\n'
        f_write.writelines(get_station_sql(item)) 
        station2id[item] = count
        count += 1
          
    f_read.close()
    f_write.close()
    return station2id

def parse_data(filepath_read, filepath_write, station2id):
    f_read = open(filepath_read, 'r')
    f_write = open(filepath_write, "a+")
    lines_r = f_read.readlines()
    route_count = 1
    tr_count = 1
    train_nums = ''
    day_u = 0
    last_time = datetime.time(0, 0)
    stops = []
    for line_r in lines_r:
        # print(line)
        if line_r == '\n':
            if(train_nums is not ''):
                f_write.writelines(get_route_sql(train_nums, \
                stops[0][0], stops[-1][0]))  
                
                for no1, stop1 in enumerate(stops):
                    f_write.writelines(get_stop_sql(route_count, stop1, no1 + 1))
                
                tr_new = tr_count + len(stops)
                f_write.writelines(get_ticket_sql(tr_count, tr_new - 1))
                tr_count = tr_new
                # reinitialize
                route_count += 1
                train_nums = ''
                day_u = 0
                last_time = datetime.time(0, 0)
                stops = []
                continue
        
        items = line_r[:-1].split()
        if(len(items) is 1):
            train_nums = items[0]
            continue
        
        if(len(items) is 4):
            stop_name = items[0]+ ' ' + items[1]
        else:
            stop_name = items[0]
        arrive_time = datetime.datetime.strptime(items[-2], '%H:%M').time()
        depart_time = datetime.datetime.strptime(items[-1], '%H:%M').time()
        temp = [station2id[stop_name], arrive_time, depart_time]
        # day convention
        if(arrive_time < last_time):
            day_u += 1
        temp.append(day_u)
        last_time = arrive_time
        if(depart_time < last_time):
            day_u += 1
        temp.append(day_u)
        last_time = depart_time
        stops.append(temp)
    
    f_write.close()
    f_read.close()

def get_filepath():
    read_folder = os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        'var', 'uploads'
    )
    write_folder = os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        'sql'
    )
    reads_path = read_folder + '/' + 'raw_station.txt'
    readr_path = read_folder + '/' + 'raw_route.txt'
    write_path = write_folder + '/' + 'data.sql'
    return reads_path, readr_path, write_path

def main(): 
    reads_path, readr_path, write_path = get_filepath()
    station2id = count_stations(reads_path, write_path)
    print(station2id['Beijing'])
    parse_data(readr_path, write_path, station2id)

if __name__=="__main__": 
    main() 
