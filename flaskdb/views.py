"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask import Blueprint, request, session, render_template, redirect, flash, url_for
import datetime
import pickle

from flaskdb import apps, db, da
from flaskdb.models import User, Item
from flaskdb.forms import AddStudentForm, LoginForm, AddItemForm, SearchItemForm, StudentRegistorForm

app = Blueprint("app", __name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("/index.html")

@app.route("/now", methods=["GET", "POST"])
def now():
    return str(datetime.datetime.now())

# This is a very danger method
@app.route("/receive", methods=["GET", "POST"])
def receive():
    if request.method == "GET":
        username = request.args.get("username")
        password = request.args.get("password")
    else:
        username = request.form["username"]
        password = request.form["password"]

    return render_template("receive.html", username=username, password=password)

@app.route("/initdb", methods=["GET", "POST"])
def initdb():
    db.drop_all()
    db.create_all()
    
    admin = User(username="admin", password="password")
    user = User(username="user", password="password")
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    return "initidb() method was executed. "

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

        if user is None or user.password != form.password.data:
            flash("Username or Password is incorrect.", "danger")
            return redirect(url_for("app.login"))

        session["username"] = user.username
        return redirect(url_for("app.index"))

    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username", None)
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("app.index"))

@app.route("/additem", methods=["GET", "POST"])
def additem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        db.session.add(item)
        db.session.commit()

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = Item.query.all()
    return render_template("additem.html", form=form, itemlist=itemlist)

@app.route("/searchitem", methods=["GET", "POST"])
def searchitem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = SearchItemForm()

    if form.validate_on_submit():
        itemlist = Item.query.filter(Item.itemname.like("%" + form.itemname.data + "%")).all()        
        return render_template("search.html", form=form, itemlist=itemlist)

        # For change to PRG
        # itemlist = pickle.dumps(itemlist)
        # session["itemlist"] = itemlist
        # return redirect(url_for("app.searchitem"))

    # if "itemlist" in session:
    #     itemlist = session["itemlist"]
    #     itemlist = pickle.loads(itemlist)
    #     session.pop("itemlist", None)
    # else:
    #     itemlist = None
    # 
    # return render_template("search.html", form=form, itemlist=itemlist)

    return render_template("search.html", form=form)

@app.route("/nativesql", methods=["GET", "POST"])
def nativesql():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        da.add_item(item)

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = da.search_items()
    return render_template("additem.html", form=form, itemlist=itemlist)

# QRコードの接続先（着離席登録）
@app.route("/studentRegistor", methods=["GET", "POST"])
def studentRegistor():
    seat_name = request.args.get('seat_name', '')
    form = StudentRegistorForm()
    return render_template("studentRegistor.html", form=form, seat_name=seat_name)

# 座席表画面
@app.route("/seatList", methods=["GET", "POST"])
def seatList():
    # post
    if request.method =="POST":
        seat_name = request.form["seat_name"]
        student_num = int(request.form["student_num"])
        open_flg = int(request.form["open_flg"])
        print(f'seat_name:{seat_name}')
        print(f'student_num:{student_num}')
        print(type(student_num))
        print(f'open_flg:{open_flg}')
        st_open_flg = da.search_open_flg_by_studnet_num(student_num=student_num)
        seat_state = da.search_state_by_seat_name(seat_name=seat_name)
        print(f'student_open_flg:{st_open_flg}')
        print(f'seat_state:{seat_state[0].state}')
        print(f'seat_student_num:{seat_state[0].student_num}')
        
        # 現在の座席状況（postで受け取ったdataで処理する前）
        ex_seat_state = seat_state[0].state
        ex_student_num = seat_state[0].student_num
        print(type(ex_student_num))
        if ex_student_num==student_num: # 受け取った座席番号に同学生がすでに登録されている場合
            if ex_seat_state==1: # 且つ、着離席状況が[着席]になっている場合
                if st_open_flg!=open_flg: #公開設定が変更ありの場合
                    # [着席]のまま（タイムスタンプ打ってるからアップデートは行う）
                    da.update_seats(student_num=student_num, seat_name=seat_name, state=1)
                else: # 公開設定がなしの場合
                    # [離席]に変更
                    da.update_seats(student_num=student_num, seat_name=seat_name, state=0)
            elif ex_seat_state==0: # 且つ、着離席状況が[離席]になっている場合
                # [着席]に変更
                da.update_seats(student_num=student_num, seat_name=seat_name, state=1)
        else: # 受け取った座席番号に違う学生がいる場合
            if ex_seat_state==1: # 且つ、着離席状況が[着席]になっている場合
                print("違う人が座っているけど.......?") # ちょっとここはとりあえずこれで
                # [着席]に変更
                da.update_seats(student_num=student_num, seat_name=seat_name, state=1)
            elif ex_seat_state==0: # 且つ、着離席状況が[離席]になっている場合
                print("且つ、着離席状況が[離席]になっている場合")
                # [着席]に変更
                da.update_seats(student_num=student_num, seat_name=seat_name, state=1)
        da.update_open_flg(student_num=student_num, open_flg=open_flg)
    seat_list = da.search_seats()
    student_list = da.search_student()
    return render_template("seatList.html", seat_list=seat_list, student_list=student_list)

# 学籍詳細
@app.route("/studentDetail", methods=["GET", "POST"])
def studentDetail():
    student_num :int = request.args.get('student_num', '')
    student_list :list = da.search_student_by_studnet_num(student_num=student_num)
    return render_template("studentDetail.html", student_list= student_list)

@app.route("/studentCreate", methods=["GET", "POST"])
def studentCreate():
    form = AddStudentForm()
    if request.method =="POST":
        student_num = int(request.form["student_num"])
        student_name = request.form["student_name"]
        study_category = request.form["study_category"]
        study_content = request.form["study_content"]
        open_flg = request.form["open_flg"]
        da.add_student(student_num=student_num, student_name=student_name, study_category=study_category, study_content=study_content, open_flg=open_flg)
        print("add student")
    return render_template("studentCreate.html", form=form)