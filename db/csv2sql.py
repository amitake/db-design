import sys
import pandas as pd

# コマンドライン引数
# リストの先頭sys.argv[0]はスクリプトの名前
csv_path = sys.argv
df = pd.read_csv(csv_path[1])
output_sql = "{}".format(csv_path[1]).replace("csv/", "sql/").replace(".csv", ".sql")

# バックスラッシュはシングルクォーテーション・ダブルクォーテーションの打ち消しに使われる
prefix_txt = \
"""DROP TABLE IF EXISTS kaoru3;
CREATE TABLE kaoru3 (
	id SERIAL PRIMARY KEY,
	name_ka VARCHAR(255),
	name_ja VARCHAR(255),
    adress VARCHAR(255),
    tel VARCHAR(255),
    open TIME,
    close TIME,
    location point,
    cat VARCHAR(255),
    url VARCHAR(255)
) without oids;
"""

with open(output_sql, "w") as f:
    f.write(prefix_txt)

with open(output_sql, "a") as f:
    for i in df.index:
        df_tmp = []
        for j in range(0, len(df.columns)):
            str_tmp = df.iloc[i, j]
            df_tmp.append(str_tmp)

        body_txt = \
"""
INSERT INTO kaoru3 (
        name_ka, name_ja, adress, tel, open, close, location, cat, url
) VALUES (
""" \
    + "    " + str(df_tmp).replace("[", "").replace("]", "") + \
");"

        f.write(body_txt)
