
import os
import re
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
## TODO: duplicated station name
## TODO: Chinese characters
## TODO: keep old search in form

def get_station_sql(stop):
    s1 = "INSERT INTO timetable_tool_stations (station_name) " \
            + "VALUES ('{}');\n".format(stop)
    # TODO; change date
    return s1

def get_route_sql(number, fromid, toid):
    s1 = "INSERT INTO timetable_tool_train_records (train_number"\
            + ", train_from_id, train_to_id"
    s2 = " VALUES ('{}', {}, {}".format(number, fromid, toid)
    s3 = s1 + ")" + s2 + ");\n"
    return s3

def get_stop_sql(tid, sid, sno):
    s1 = "INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no) "\
        + "VALUES ({}, {}, {});\n".format(tid, sid, sno)
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
    for line_r in lines_r:
        # print(line)
        if line_r == '\n':
            continue
        items = line_r[:-1].split('|')
        train_nums = items[0].split(',')
        stops = items[1].split(', ')
        stop1s = []
        stop2s = []
        for stop in stops:
            stop_info = re.split('[/(/)(/)]',stop)
            station_id = station2id[stop_info[0]]
            stop_dir = stop_info[1]
            arrive_time1 = stop_info[2] # TODO
            depart_time1 = stop_info[3]
            arrive_time2 = stop_info[5]
            depart_time2 = stop_info[6]
            if(stop_dir != 'u'):
                stop1s.append(station_id)
            if(stop_dir != 'd'):
                stop2s.append(station_id)
        
        stop2s = stop2s[::-1]
        f_write.writelines(get_route_sql(train_nums[0], \
                stop1s[0], stop1s[-1]))  
        for no1, stop1 in enumerate(stop1s):
            f_write.writelines(get_stop_sql(count, stop1, no1 + 1))
        count += 1
        

        f_write.writelines(get_route_sql(train_nums[1], \
                stop2s[0], stop2s[-1])) 
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
