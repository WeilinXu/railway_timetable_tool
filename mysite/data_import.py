
import os
import re
import datetime 

'''
record sytle:
see files in /var/upload
'''
def get_group_sql(group_name):
    s0 = "INSERT INTO timetable_tool_station_groups (city_name) " \
            + "VALUES ('{}');\n".format(group_name) 
    return s0

def get_station_sql(stop, stop_cn, group_id):
    s1 = "INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) " \
            + "VALUES ('{}', '{}', {});\n".format(stop, stop_cn, group_id) 
    return s1

def get_route_sql(number, fromid, toid):
    s1 = "INSERT INTO timetable_tool_train_records (train_number"\
            + ", train_from_id, train_to_id"
    s2 = " VALUES ('{}', {}, {}".format(number, fromid, toid)
    s3 = s1 + ")" + s2 + ");\n"
    return s3

def get_stop_sql(tid, s_info, sno):
    s1 = "INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, "\
        + "arr_time, arr_day, dep_time, dep_day, km) " \
        + "VALUES ({}, {}, {}, '{}', {}, '{}', {}, {});\n".format( \
        tid, s_info[0], sno, s_info[1], s_info[3], s_info[2], s_info[4], s_info[5])
    return s1

def get_ticket_sql(tr_id1, tr_id2, ticket_date = '2020-05-05', tickets_avaliable = 5):
    s1 = "INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, "\
        + "tickets_avaliable) VALUES ({}, {}, '{}', {});\n".format(tr_id1, tr_id2, ticket_date, tickets_avaliable)
    return s1

def count_stations(filepath_read, filepath_write):
    station2id = {}
    station2id_cn = {}
    f_read = open(filepath_read, 'r')
    f_write = open(filepath_write, 'w')
    lines_r = f_read.readlines()
    count = 1
    group_count = 0
    for line_r in lines_r:
        if line_r == '\n':
            continue
        items = line_r[:-1].split()
        if(len(items) is 3):
            items[1] = items[1] + ' ' + items[2]
        if(items[0][0] == '-'):  # station of the same city
            items[0] = items[0][1:]
        else:
            f_write.writelines(get_group_sql(items[1])) 
            group_count += 1

        f_write.writelines(get_station_sql(items[1], items[0], group_count)) 
        station2id[items[1]] = count
        station2id_cn[items[0]] = count
        count += 1
          
    f_read.close()
    f_write.close()
    return station2id, station2id_cn

def parse_data(filepath_read, filepath_write, station2id, station2id_cn):
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
            print(train_nums)
            continue
        
        if(len(items) is 5):
            stop_name = items[0]+ ' ' + items[1]
        else:
            stop_name = items[0]
        arrive_time = datetime.datetime.strptime(items[-3], '%H:%M').time()
        depart_time = datetime.datetime.strptime(items[-2], '%H:%M').time()
        if(stop_name in station2id):
            stop_station_id = station2id[stop_name]
        elif(stop_name in station2id_cn):
            stop_station_id = station2id_cn[stop_name]
        else:
            stop_station_id = -1
            print("Error: no such station in table!")
        temp = [stop_station_id, arrive_time, depart_time]
        # day convention
        if(arrive_time < last_time):
            day_u += 1
        temp.append(day_u)
        last_time = arrive_time
        if(depart_time < last_time):
            day_u += 1
        temp.append(day_u)
        temp.append(int(items[-1]))
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
    station2id, station2id_cn = count_stations(reads_path, write_path)
    print(station2id['Beijing'])
    parse_data(readr_path, write_path, station2id, station2id_cn)

if __name__=="__main__": 
    main() 
