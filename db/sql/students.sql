DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_num INT,
    student_name VARCHAR(255),
    study_category VARCHAR(255),
    open_flg INT,
    study_content VARCHAR(255)) without oids;
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2022058, '竹中亜瞳', '画像処理', 1, '人物検出を用いたマーチングプレイヤーの位置情報による練習補助システムの構築');
