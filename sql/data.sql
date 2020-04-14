INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Beijing');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Beijing', '北京', 1);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Beijing West', '北京西', 1);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Beijing East', '北京东', 1);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Changping North', '昌平北', 1);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Zhangjiakou');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Zhangjiakou', '张家口', 2);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Datong');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Datong', '大同', 3);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Jining South');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Jining South', '集宁南', 4);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Hohhot');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Hohhot', '呼和浩特', 5);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Hohhot East', '呼和浩特东', 5);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Baotou');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Baotou', '包头', 6);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Baotou East', '包头东', 6);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Wuhai');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Wuhai', '乌海', 7);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Wuhai West');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Wuhai West', '乌海西', 8);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Yinchuan');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Yinchuan', '银川', 9);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Zhongwei');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Zhongwei', '中卫', 10);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Tianjin');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Tianjin', '天津', 11);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Tianjin West', '天津西', 11);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Dezhou');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Dezhou', '德州', 12);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Jinan');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Jinan', '济南', 13);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Daminghu', '大明湖', 13);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Xuzhou');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Xuzhou', '徐州', 14);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Bengbu');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Bengbu', '蚌埠', 15);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Nanjing');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Nanjing', '南京', 16);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Wuxi');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Wuxi', '无锡', 17);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Suzhou');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Suzhou', '苏州', 18);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Shanghai');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Shanghai', '上海', 19);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Shanghai South', '上海南', 19);
INSERT INTO timetable_tool_station_groups (city_name) VALUES ('Hangzhou');
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Hangzhou', '杭州', 20);
INSERT INTO timetable_tool_stations (station_name, station_name_cn, group_city_id) VALUES ('Hangzhou East', '杭州东', 20);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K263', 1, 10);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 1, 1, '09:25:00', 0, '09:25:00', 0, 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 5, 2, '12:53:00', 0, '13:00:00', 0, 196);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 6, 3, '15:55:00', 0, '16:07:00', 0, 374);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 7, 4, '17:42:00', 0, '17:48:00', 0, 501);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 9, 5, '19:11:00', 0, '19:18:00', 0, 651);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 8, 6, '19:31:00', 0, '19:43:00', 0, 659);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 11, 7, '21:35:00', 0, '21:38:00', 0, 808);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (1, 10, 8, '21:54:00', 0, '21:54:00', 0, 824);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (1, 8, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K264', 10, 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 10, 1, '20:05:00', 0, '20:05:00', 0, 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 11, 2, '20:20:00', 0, '20:24:00', 0, 16);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 8, 3, '21:58:00', 0, '22:12:00', 0, 165);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 9, 4, '22:24:00', 0, '22:32:00', 0, 173);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 7, 5, '23:55:00', 0, '00:01:00', 1, 323);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 6, 6, '01:46:00', 1, '01:57:00', 1, 450);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 5, 7, '04:27:00', 1, '04:38:00', 1, 628);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (2, 1, 8, '08:21:00', 1, '08:21:00', 1, 824);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (9, 16, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K89', 2, 8);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (3, 2, 1, '22:17:00', 0, '22:17:00', 0, 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (3, 5, 2, '01:32:00', 1, '01:39:00', 1, 190);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (3, 6, 3, '04:19:00', 1, '04:27:00', 1, 368);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (3, 7, 4, '06:04:00', 1, '06:10:00', 1, 495);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (3, 9, 5, '07:33:00', 1, '07:41:00', 1, 645);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (3, 8, 6, '07:57:00', 1, '07:57:00', 1, 653);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (17, 22, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K90', 8, 2);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (4, 8, 1, '21:42:00', 0, '21:42:00', 0, 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (4, 9, 2, '21:54:00', 0, '22:00:00', 0, 8);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (4, 7, 3, '23:25:00', 0, '23:35:00', 0, 158);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (4, 6, 4, '01:25:00', 1, '01:39:00', 1, 285);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (4, 5, 5, '04:00:00', 1, '04:11:00', 1, 463);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (4, 2, 6, '07:30:00', 1, '07:30:00', 1, 653);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (23, 28, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('Z284/Z281', 10, 28);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 10, 1, '06:51:00', 0, '06:51:00', 0, 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 11, 2, '07:06:00', 0, '07:10:00', 0, 16);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 8, 3, '08:49:00', 0, '08:56:00', 0, 165);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 9, 4, '09:08:00', 0, '09:29:00', 0, 173);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 7, 5, '10:40:00', 0, '10:46:00', 0, 323);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 6, 6, '12:27:00', 0, '12:39:00', 0, 450);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 5, 7, '15:06:00', 0, '15:17:00', 0, 628);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 1, 8, '18:31:00', 0, '19:10:00', 0, 824);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 17, 9, '20:26:00', 0, '20:40:00', 0, 972);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 21, 10, '02:14:00', 1, '02:35:00', 1, 1638);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 22, 11, '03:54:00', 1, '03:57:00', 1, 1802);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 23, 12, '05:30:00', 1, '05:38:00', 1, 1986);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 24, 13, '07:25:00', 1, '07:30:00', 1, 2161);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 25, 14, '07:58:00', 1, '08:01:00', 1, 2203);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 27, 15, '09:54:00', 1, '10:20:00', 1, 2301);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (5, 28, 16, '12:23:00', 1, '12:23:00', 1, 2474);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (29, 44, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('Z282/Z283', 28, 10);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 28, 1, '17:04:00', 0, '17:04:00', 0, 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 27, 2, '18:54:00', 0, '19:30:00', 0, 173);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 25, 3, '20:25:00', 0, '20:30:00', 0, 271);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 24, 4, '20:52:00', 0, '20:55:00', 0, 313);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 23, 5, '22:48:00', 0, '22:55:00', 0, 488);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 22, 6, '00:27:00', 1, '00:33:00', 1, 672);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 21, 7, '02:10:00', 1, '02:17:00', 1, 836);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 18, 8, '06:54:00', 1, '07:03:00', 1, 1273);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 17, 9, '09:03:00', 1, '09:06:00', 1, 1502);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 1, 10, '10:22:00', 1, '11:07:00', 1, 1650);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 5, 11, '14:22:00', 1, '14:28:00', 1, 1846);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 6, 12, '17:07:00', 1, '17:17:00', 1, 2024);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 7, 13, '18:54:00', 1, '19:00:00', 1, 2151);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 9, 14, '20:09:00', 1, '20:29:00', 1, 2301);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 8, 15, '20:43:00', 1, '20:51:00', 1, 2309);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 11, 16, '22:05:00', 1, '22:09:00', 1, 2458);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day, km) VALUES (6, 10, 17, '22:26:00', 1, '22:26:00', 1, 2474);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (45, 61, '2020-05-05', 5);
