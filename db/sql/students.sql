DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_num INT,
    student_name VARCHAR(255),
    study_category VARCHAR(255),
    open_flg INT,
    study_content VARCHAR(255)) without oids;
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2022058, '竹中亜瞳', '画像処理', 1, '人物検出を用いたマーチングプレイヤーの位置情報による練習補助システムの構築');
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2322001, '青井葦人', '自然言語処理', 1, 'サッカープレイヤーのプレイの言語化と技術向上曲線のなんちゃら');
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2322002, '福岡太郎', 'VR', 1, 'なんちゃらこうちゃら');
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2322003, '緑谷出久', '画像処理', 1, '個性認識システムの構築');
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2322004, '爆豪勝己', '自然言語処理', 1, '爆発');
INSERT INTO students (student_num, student_name, study_category, open_flg, study_content) VALUES (2322005, '金木研', 'データベース', 1, '白金木');