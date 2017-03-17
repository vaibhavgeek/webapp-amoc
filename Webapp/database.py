import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, LargeBinary
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Students(Base):
	__tablename__ = 'student'

	id = Column(Integer, primary_key=True)
	rollno = Column(String(250), nullable=False)
	password = Column(String(100), nullable=False)
	name = Column(String(100))
	image = Column(LargeBinary)
	time_created = Column(DateTime(timezone=True), server_default=func.now())

class Courses(Base):
	__tablename__ = 'course'
	id = Column(Integer,primary_key=True)
	course_code = Column(String(250))
	course_name_long = Column(String)
	course_name_short = Column(String)
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	year = Column(String)
	branch = Column(String)
	year = Column(String)
	semester = Column(String)
	#Owner_id = Column(Integer,ForeignKey('user.id'))
	#user = relationship(Users)

class TimeTable(Base):
	"""docstring for ClassName"""
	__tablename__ = 'timetable'

	id = Column(Integer, primary_key=True)
	course_id = Column(Integer, ForeignKey('course.id'))
	day = Column(String)
	time = Column(String)
	branch_code = Column(String)
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	course_rel = relationship(Courses)

class Attendence(Base):
	__tablename__ = 'attendence'
	id = Column(Integer, primary_key=True)
	present = Column(String)
	date = Column(String, nullable=False)
	timetable_id = Column(Integer, ForeignKey('timetable.id')) 
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	timetable_rel = relationship(TimeTable)

engine = create_engine('sqlite:///Blog.db')


Base.metadata.create_all(engine)