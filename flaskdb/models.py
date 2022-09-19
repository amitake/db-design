"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flaskdb import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    itemname = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return "<Item %r>" % self.id

class Seat(db.Model):
    __tablename__ = "seats"
    id = db.Column(db.Integer, primary_key=True)
    seat_name = db.Column(db.String(128), nullable=False)
    student_num = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "<Seat %r>" % self.id

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    student_num = db.Column(db.Integer, nullable=False)
    student_name = db.Column(db.String(128), nullable=False)
    study_category = db.Column(db.String(128), nullable=False)
    open_flg = db.Column(db.Integer, nullable=False)
    study_content = db.Column(db.String(128), nullable=False)
    def __repr__(self):
        return "<Student %r>" % self.id