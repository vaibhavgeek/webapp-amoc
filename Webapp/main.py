from flask import Flask, request, jsonify
import os
from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from rollno_parse import main
from database import Base, Courses, Attendence, TimeTable, Students

app = Flask(__name__)
engine = create_engine('sqlite:///amoc.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
Session = scoped_session(DBSession)
sessions = Session()


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
def Courses(rollno):
    valuebsr = main(rollno)
	# passing the rollno in a function and checking whether its valid or not
    if main(rollno) is False:
		# returning json object of Error due to wrong roll no
        return jsonify(Error={'invalid rollno': 'invalid'})
    else:
        Course = sessions.query(Courses).filter_by(
            branch=valuebsr[0], semester=valuebsr[1])
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


if __name__ == '__main__':
    app.secret_key = "unknown_cookie_values_present_here_so_that_it_remains_secret_so_dont worry_its still secret"
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
