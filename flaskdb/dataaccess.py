"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from psycopg2 import sql, connect, ProgrammingError
import flaskdb.var as v
from flaskdb.models import Item, Seat, Student

class DataAccess:

    # Constractor called when this class is used. 
    # It is set for hostname, port, dbname, useranme and password as parameters.
    def __init__(self, hostname, port, dbname, username, password):
        self.dburl = "host=" + hostname + " port=" + str(port) + \
                     " dbname=" + dbname + " user=" + username + \
                     " password=" + password

    # This method is used to actually issue query sql to database. 
    def execute(self, query, autocommit=True):
        with connect(self.dburl) as conn:
            if v.SHOW_SQL:
                print(query.as_string(conn))
            conn.autocommit = autocommit
            with conn.cursor() as cur:
                cur.execute(query)
                if not autocommit:
                    conn.commit()
                try:
                    return cur.fetchall()
                except ProgrammingError as e:
                    return None

    # For mainly debug, This method is used to show sql to be issued to database. 
    def show_sql(self, query):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))

    # search item data
    def search_items(self):
        query = sql.SQL("""
            SELECT * FROM \"items\"
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.user_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list

    # search item data by itemname
    def search_items_by_itemname(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE itemname LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.user_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list

    def add_item(self, item):
        query = sql.SQL("""
            INSERT INTO \"items\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("items"),
            fields = sql.SQL(", ").join([
                sql.Identifier("itemname"),
                sql.Identifier("price")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(item.itemname),
                sql.Literal(item.price)
            ])
        )
        self.execute(query, autocommit=True)
        
    # search seat data
    def search_seats(self):
        query = sql.SQL("""
            SELECT * FROM \"seats\" ORDER BY seat_name
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        seat_list = []
        for r in results:
            seat = Seat()
            seat.id = r[0]
            seat.seat_name = r[1]
            seat.student_num = r[2]
            seat.time = r[3]
            seat.state = r[4]
            seat_list.append(seat)
        return seat_list
    
    # search student data by student_num
    def search_student_by_studnet_num(self, student_num):
        query = sql.SQL("""
            SELECT * FROM \"students\" WHERE student_num={student_num}
        """).format(
            student_num = sql.Literal(student_num)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        student_list = []
        for r in results:
            student = Student()
            student.id = r[0]
            student.student_num = r[1]
            student.student_name = r[2]
            student.study_category = r[3]
            student.open_flg = r[4]
            student_list.append(student)
        return student_list

    # search student data by student_num
    def search_open_flg_by_studnet_num(self, student_num):
        query = sql.SQL("""
            SELECT open_flg FROM \"students\" WHERE student_num={student_num}
        """).format(
            student_num = sql.Literal(student_num)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        open_flgs = []
        for r in results:
            student = Student()
            student.open_flg = r[0]
        print(student.open_flg)
        return student.open_flg
    
        # search student data by student_num
    def search_state_by_seat_name(self, seat_name):
        query = sql.SQL("""
            SELECT state FROM \"seats\" WHERE seat_name={seat_name}
        """).format(
            seat_name = sql.Literal(seat_name)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        states = []
        for r in results:
            seat = Seat()
            seat.state = r[0]
        print(seat.state)
        return seat.state
    
    # update seats data 
    def update_open_flg(self, student_num, open_flg):
        query = sql.SQL("""
            UPDATE \"students\" SET open_flg={open_flg} WHERE student_num={student_num}
        """).format(
            open_flg = sql.Literal(open_flg),
            student_num = sql.Literal(student_num)
        )
        # self.show_sql(query)
        self.execute(query, autocommit=True)
        
        # update seats data 
    def update_seats(self, student_num, seat_name, state):
        query = sql.SQL("""
            UPDATE \"seats\" SET student_num={student_num}, time=now(), state={state} WHERE seat_name={seat_name}
        """).format(
            student_num = sql.Literal(student_num),
            state = sql.Literal(state),
            seat_name = sql.Literal(seat_name)    
        )
        # self.show_sql(query)
        self.execute(query, autocommit=True)