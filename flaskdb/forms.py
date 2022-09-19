"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, HiddenField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import ButtonField

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="User Name is required."),
            length(max=64, message="User Name should be input within 64 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="Password is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.username = self.username.data
        user.password = self.password.data

class AddItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    price = IntegerField(
        "Price",
        validators = [
            DataRequired(message="Price is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname
        self.price.data = item.price

    def copy_to(self, item):
        item.itemname = self.itemname.data
        item.price = self.price.data

class SearchItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname

    def copy_to(self, item):
        item.itemname = self.itemname.data

class StudentRegistorForm(FlaskForm):
    seat_name = HiddenField(
        "Seat Name",
        validators = [
            DataRequired(message="Seat Name is required."),
        ],
    )
    student_num = IntegerField(
        "Student Number",
        validators = [
            DataRequired(message="Student Number is required."),
        ],
    )
    open_flg = RadioField(
        "Open Flg",
        validators = [
            DataRequired(message="Open Flg is required."),
        ],
        choices=[('1', '公開'), ('0', '非公開')]
        
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, seat):
        self.seat_name.data = seat.seat_name
        self.student_num.data = seat.student_num
        self.open_flg = seat.open_flg

    def copy_to(self, seat):
        seat.seat_name = self.seat_name.data
        seat.student_num = self.student_num.data
        seat.open_flg = self.open_flg.data
        
class AddStudentForm(FlaskForm):
    student_num = StringField(
        "Student Number",
        validators = [
            DataRequired(message="Student Number is required."),
        ],
    )
    student_name = StringField(
        "Student Name",
        validators = [
            DataRequired(message="Student Name is required."),
        ],
    )
    study_category = StringField(
        "Study Category",
        validators = [
            DataRequired(message="Study Category is required."),
        ],
    )
    study_content = StringField(
        "Study Content",
        validators = [
            DataRequired(message="tudy content is required."),
        ],
    )
    open_flg = RadioField(
        "Open Flg",
        validators = [
            DataRequired(message="Open Flg is required."),
        ],
        choices=[('1', '公開'), ('0', '非公開')]
        
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, student):
        self.student_num.data = student.student_num
        self.student_name.data = student.student_name
        self.study_category.data = student.study_category
        self.study_content.data = student.study_content
        self.open_flg.data = student.open_flg

    def copy_to(self, student):
        student.student_num = self.student_num.data
        student.student_name = self.student_name.data
        student.study_category = self.study_category.data
        student.study_content = self.study_content.data
        student.open_flg = self.open_flg.data