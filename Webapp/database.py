import os
import sys
from flask import Flask
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blog.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))
    image = db.Column(db.LargeBinary)
    time_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())

    def __init__(self, rollno, password, name, time_created):
        self.rollno = rollno
        self.password = password
        self.name = name
        self.time_created = time_created

    def __repr__(self):
        return '<Post %r>' % self.name


class Courses(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(250))
    course_name_long = db.Column(db.String)
    course_name_short = db.Column(db.String)
    time_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    year = db.Column(db.String)
    branch = db.Column(db.String)
    semester = db.Column(db.String)

    #Owner_id = db.Column(db.Integer,ForeignKey('user.id'))
    #user = relationship(Users)


class TimeTable(db.Model):
    """docstring for ClassName"""
    __tablename__ = 'timetable'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    day = db.Column(db.String)
    time = db.Column(db.String)
    branch_code = db.Column(db.String)
    time_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    course_rel = db.relationship('Courses')


class Attendence(db.Model):
    __tablename__ = 'attendence'
    id = db.Column(db.Integer, primary_key=True)
    present = db.Column(db.String)
    date = db.Column(db.String, nullable=False)
    timetable_id = db.Column(db.Integer, db.ForeignKey('timetable.id'))
    time_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    timetable_rel = db.relationship('TimeTable')


@property
def serialize(self):
    return {
        # courses
        'id': self.id,
        'course_code': self.course_code,
        'course_name_long': self.course_name_long,
        'course_name_short': self.course_name_short,
        'year': self.year,
        'branch': self.branch,
        'semester': self.semester,
        # TimeTable
        'course_id': self.course_id,
        'day': self.day,
        'time': self.time,
        'branch_code': self.branch_code,


        'time_created': self.time_created,

    }


@property
def error(self):
    return {
        'invalid_rollno': self.rollno
    }
