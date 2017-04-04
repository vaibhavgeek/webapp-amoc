from flask import Flask,request
import os
from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import requests
from flask_restful import Resource, Api
from BeautifulSoup import BeautifulSoup

api = Api(app)
app = Flask(__name__)

engine = create_engine('sqlite:///amoc.db')

@app.route('/')
@app.route('/index')
def Index():
	return "index files"

@app.route('/login', methods=['GET','POST'])
def Login():
	if request.method == 'POST':
		username = request.form["username"]
		password = request.form["password"]
		return login(username,password)
	else:
		return "Parameters not found for login"

@app.route('/students/<rollno>/course_name')
def Courses(rollno):
	return "Courses info is here"

@app.route('/students/<rollno>/time_table')
def Time_table(rollno):
	return "Time table here"

@app.route('/students/<rollno>/attendence')
def Attendence(rollno):
	return "Attendence here"

@app.route('/students/<rollno>/courses/course_code')
def Course_code(rollno):
	return "Course code here"

@app.route('/students/<rollno>/courses/course_code/syllabus')
def Syllabus(rollno):
	return "syllabus here"

@app.route('/students/<rollno>')
def Rollno():
	return "rollno"


@app.route('/signup', methods = ['GET','POST'])
def Signup():
	if request.method == 'POST':
		return "post method used"

	return "Signup here"

@app.route('/students/<rollno>/edit', methods=['GET','POST'])
def Edit():
	if request.method == 'POST':
		return "editted data here"
	return "Edit here"



def login(username, password):
	data = {
	'mode':'191',
	'username':username,
	'password':password,
	'a':'1439199700564',
	'producttype':'0'
	}
	send=requests.post('http://172.50.1.1:8090/login.xml',data=data).text
	soup = BeautifulSoup(send)
	if soup.message.string == "You have successfully logged in" or soup.message.string == "You have reached Maximum Login Limit.":
		return "true"
	else:
		return "false"

if __name__ == '__main__':
	app.secret_key = "unknown_cookie_values_present_here_so_that_it_remains_secret_so_dont worry_its still secret"
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)	
	