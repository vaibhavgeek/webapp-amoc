from flask import Flask, request, jsonify
from rollno_parse import main
from database import Courses, Attendence, TimeTable, Students
from flask_migrate import Migrate
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blog.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
@app.route('/index')
def Index():
	return "index files"


@app.route('/login', methods=['GET', 'POST'])
def Login():
	if request.method == 'POST':
		return 'login data here'
	return "login information up here"


# making api endpoint for Courses
@app.route('/students/<rollno>/odd/course_name')
def Course_details(rollno):
	valuebsr = main(rollno)
	# passing the rollno in a function and checking whether its valid or not
	if main(rollno) is False:
		# returning json object of Error due to wrong roll no
		return jsonify(Error={'invalid rollno': 'invalid'})
	else:
		Course = Courses.query.all()
		return jsonify(Course_details=[i.serialize for i in Course])


@app.route('/students/<rollno>/odd/time_table')
def Time_table(rollno):
	valuebsr = main(rollno)
	# passing the rollno in a function and checking whether its valid or not
	if main(rollno) is False:
		# returning json object of Error due to wrong roll no
		return jsonify(Error={'invalid rollno': 'invalid'})




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


@app.route('/signup', methods=['GET', 'POST'])
def Signup():
	if request.method == 'POST':
		return "post method used"

	return "Signup here"


@app.route('/students/<rollno>/edit', methods=['GET', 'POST'])
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
