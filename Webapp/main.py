from flask import Flask, request, jsonify
import os
from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from rollno_parse import main
from database import Base, Courses, Attendence, TimeTable, Students, serialize
from flask_migrate import Migrate


app = Flask(__name__)
engine = create_engine('sqlite:///amoc.db')
migrate = Migrate(app, engine)
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
        username = request.form.get("username")
        password = request.form.get('password')
        return username

    return "login information up here"


# making api endpoint for Courses
@app.route('/students/<rollno>/course_name')
def Course(rollno):
    valuebsr = main(rollno)
    # passing the rollno in a function and checking whether its valid or not
    if main(rollno) is False:
        # returning json object of Error due to wrong roll no
        return jsonify(Error={'invalid rollno': 'invalid'})
    else:
        Course_details = sessions.query(Courses).all()
        return jsonify(Course_detail=[i.serialize for i in Course_details])


@app.route('/students/<rollno>/time_table')
def Time_table(rollno):
    valuebsr = main(rollno)
    # passing the rollno in a function and checking whether its valid or not
    if main(rollno) is False:
        # returning json object of Error due to wrong roll no
        return jsonify(Error={'invalid rollno': 'invalid'})
    else:
        Course = sessions.query(Courses).filter_by(semester=valuebsr[1],
                                                   branch='valuebsr[0]').one()
        Timetable = sessions.query(TimeTable).filter_by(course_rel=Course)

        return jsonify(TimeTable=[i.serialize for i in Timetable])


@app.route('/students/<rollno>/attendence')
def Attendence(rollno):
    return "Attendence here"


@app.route('/students/<rollno>/courses/course_code')
def Course_code(rollno):
    # passing the rollno in a function and checking whether its valid or not
    if main(rollno) is False:
        # returning json object of Error due to wrong roll no
        return jsonify(Error={'invalid rollno': 'invalid'})
    else:
        Course = sessions.query(Courses).filter_by(semester=valuebsr[1])


@app.route('/students/<rollno>/courses/course_code/syllabus')
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
        'mode': '191',
        'username': username,
        'password': password,
        'a': '1439199700564',
        'producttype': '0'
    }
    send = requests.post('http://172.50.1.1:8090/login.xml', data=data).text
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
