DROP TABLE IF EXISTS seats;
CREATE TABLE seats (
    id SERIAL PRIMARY KEY,
    seat_name VARCHAR(255),
    student_num INT,
    time TIMESTAMP,
    state INT) without oids;
INSERT INTO seats (seat_name, student_num, time, state) VALUES ('j1_6_a1', 2022058, now(), 1);
INSERT INTO seats (seat_name, student_num, time, state) VALUES ('j1_6_a2', 0, now(), 0);
INSERT INTO seats (seat_name, student_num, time, state) VALUES ('j1_6_a3', 0, now(), 0);
INSERT INTO seats (seat_name, student_num, time, state) VALUES ('j1_6_a4', 0, now(), 0);
INSERT INTO seats (seat_name, student_num, time, state) VALUES ('j1_6_a5', 0, now(), 0);
INSERT INTO seats (seat_name, student_num, time, state) VALUES ('j1_6_a6', 0, now(), 0);