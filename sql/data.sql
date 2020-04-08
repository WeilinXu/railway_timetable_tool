INSERT INTO timetable_tool_stations (station_name) VALUES ('Beijing');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Zhangjiakou');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Datong');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Jining South');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Hohhot');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Hohhot East');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Baotou East');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Baotou');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Linhe');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Wuhai');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Wuhai West');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Shizuishan');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Yinchuan');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Zhongwei');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Baiyin West');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Lanzhou');
INSERT INTO timetable_tool_stations (station_name) VALUES ('Beijing West');
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K263', 1, 8);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 1, 1, '09:25:00', 0, '09:25:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 2, 2, '12:53:00', 0, '13:00:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 3, 3, '15:55:00', 0, '16:07:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 4, 4, '17:42:00', 0, '17:48:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 6, 5, '19:11:00', 0, '19:18:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 5, 6, '19:31:00', 0, '19:43:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 7, 7, '21:35:00', 0, '21:38:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (1, 8, 8, '21:54:00', 0, '21:54:00', 0);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (1, 8, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K264', 8, 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 8, 1, '20:05:00', 0, '20:05:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 7, 2, '20:20:00', 0, '20:24:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 5, 3, '21:58:00', 0, '22:12:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 6, 4, '22:24:00', 0, '22:32:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 4, 5, '23:55:00', 0, '00:01:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 3, 6, '01:46:00', 1, '01:57:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 2, 7, '04:27:00', 1, '04:38:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (2, 1, 8, '08:21:00', 1, '08:21:00', 1);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (9, 16, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K89', 17, 5);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (3, 17, 1, '22:17:00', 0, '22:17:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (3, 2, 2, '01:32:00', 1, '01:39:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (3, 3, 3, '04:19:00', 1, '04:27:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (3, 4, 4, '06:04:00', 1, '06:10:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (3, 6, 5, '07:33:00', 1, '07:41:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (3, 5, 6, '07:57:00', 1, '07:57:00', 1);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (17, 22, '2020-05-05', 5);
INSERT INTO timetable_tool_train_records (train_number, train_from_id, train_to_id) VALUES ('K90', 5, 17);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (4, 5, 1, '21:42:00', 0, '21:42:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (4, 6, 2, '21:54:00', 0, '22:00:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (4, 4, 3, '23:25:00', 0, '23:35:00', 0);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (4, 3, 4, '01:25:00', 1, '01:39:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (4, 2, 5, '04:00:00', 1, '04:11:00', 1);
INSERT INTO timetable_tool_stop_records (train_record_id, station_id, station_no, arr_time, arr_day, dep_time, dep_day) VALUES (4, 17, 6, '07:30:00', 1, '07:30:00', 1);
INSERT INTO timetable_tool_tickets (stop_from_id, stop_to_id, train_date, tickets_avaliable) VALUES (23, 28, '2020-05-05', 5);