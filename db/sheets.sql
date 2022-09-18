DROP TABLE IF EXISTS sheets;
CREATE TABLE sheets (
    sheet_id SERIAL PRIMARY KEY,
    sheet_name VARCHAR(255),
    student_num INT,
    time TIMESTAMP,
    statue INT) without oids;
INSERT INTO sheets (sheet_name, student_num, time, statue) VALUES ('j1_6_a1', 2022058, now(), 1);
INSERT INTO sheets (sheet_name, student_num, time, statue) VALUES ('j1_6_a2', 0, now(), 0);
INSERT INTO sheets (sheet_name, student_num, time, statue) VALUES ('j1_6_a3', 0, now(), 0);
INSERT INTO sheets (sheet_name, student_num, time, statue) VALUES ('j1_6_a4', 0, now(), 0);
INSERT INTO sheets (sheet_name, student_num, time, statue) VALUES ('j1_6_a5', 0, now(), 0);
