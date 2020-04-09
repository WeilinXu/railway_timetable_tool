
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
        + "VALUES ({}, {}, {}, {}, {}, {}, {});\n".format(tid, s_info[0], sno, s_info[1], s_info[3], s_info[2], s_info[4])
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
    count = 1
    last_time = datetime.time(0, 0)
    day_u = 0
    

    for line_r in lines_r:
        # print(line)
        if line_r == '\n':
            continue
        items = line_r[:-1].split('|')
        train_nums = items[0].split(',')
        stops = items[1].split(', ')
        stop1s = []
        stop2s_old = []
        for stop in stops:
            stop_info = re.split('[/(/)(/)]',stop)
            station_id = station2id[stop_info[0]]
            stop_dir = stop_info[1]
            arrive_time1 = datetime.datetime.strptime(stop_info[2], '%H:%M').time()
            depart_time1 = datetime.datetime.strptime(stop_info[3], '%H:%M').time()
            arrive_time2 = datetime.datetime.strptime(stop_info[5], '%H:%M').time()
            depart_time2 = datetime.datetime.strptime(stop_info[6], '%H:%M').time()
            if(stop_dir != 'u'):
                temp = [station_id, arrive_time1, depart_time1]
                # day convention for up direction
                if(arrive_time1 < last_time):
                    day_u += 1
                temp.append(day_u)
                last_time = arrive_time1
                if(depart_time1 < last_time):
                    day_u += 1
                temp.append(day_u)
                last_time = depart_time1
                stop1s.append(temp)

            if(stop_dir != 'd'):
                temp = [station_id, arrive_time2, depart_time2]
                stop2s_old.append(temp)
        
        stop2s_old = stop2s_old[::-1]
        # day convention for down direction
        last_time = datetime.time(0, 0)
        day_d = 0
        stop2s = []
        for stop_record in stop2s_old:
            temp = [stop_record[0], stop_record[1], stop_record[2]]
            if(stop_record[1] < last_time):
                day_d += 1
            temp.append(day_d)
            last_time = stop_record[1]
            if(stop_record[2] < last_time):
                day_d += 1
            temp.append(day_d)
            last_time = stop_record[2]
            stop2s.append(temp)

        f_write.writelines(get_route_sql(train_nums[0], \
                stop1s[0][0], stop1s[-1][0]))  
        for no1, stop1 in enumerate(stop1s):
            f_write.writelines(get_stop_sql(count, stop1, no1 + 1))
        count += 1
        

        f_write.writelines(get_route_sql(train_nums[1], \
                stop2s[0][0], stop2s[-1][0])) 
        for no2, stop2 in enumerate(stop2s):
            f_write.writelines(get_stop_sql(count, stop2, no2 + 1))
        count += 1

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
