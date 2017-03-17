from flask import Flask,request
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def Index():
	return "index files"

@app.route('/login', methods=['GET','POST'])
def Login():
	if request.method == 'POST':
		return 'login data here'
	return "login information up here"

@app.route('/students/<rollno>/odd/course_name')
def Courses(rollno):
	return "Courses info is here"

@app.route('/students/<rollno>/odd/time_table')
def Time_table(rollno):
	return "Time table here"

@app.route('/students/<rollno>/odd/attendence')
def Attendence(rollno):
	return "Attendence here"

@app.route('/students/<rollno>/odd/courses/course_code')
def Course_code(rollno):
	return "Course code here"

@app.route('/students/<rollno>/odd/courses/course_code/syllabus')
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



if __name__ == '__main__':
	app.secret_key = "unknown_cookie_values_present_here_so_that_it_remains_secret_so_dont worry_its still secret"
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)	
	