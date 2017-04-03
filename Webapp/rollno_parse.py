import datetime


def main(rollno):
    roll_no = rollno.upper()
    now = datetime.datetime.now()
    # parsing the year,branch
    engineering = roll_no[0]
    year = roll_no[1:3]
    branch = roll_no[3:5]
    roll_no = roll_no[5:]
    if valid(engineering, year, branch, roll_no) == 'done!':
        # making the parse  data as a year
        Rollno_year = '20' + str(year)
        present_year = now.year
        # calculating the present year
        student_year = present_year - int(Rollno_year)
        if student_year == 0:
            student_sem = 1
            return branch, student_sem
        elif now.month <= 6:
            student_sem = student_year * 2
            return branch, student_sem, roll_no
        else:
            student_sem = student_year * 2 - 1
            return branch, student_sem, roll_no
    else:
        return False


def valid(engineering, year, branch, roll_no):
    # checking whether a user is valid or not
    headers = {'engineering': {'U', 'I'},
               'year': {'12', '13', '14', '15', '16', '17'},
               'branch': {'CO', 'CE', 'ME', 'CH', 'EE', 'EC', 'MA', 'CY', 'PH'}}
    value1 = engineering in headers.get('engineering')
    value2 = year in headers.get('year')
    value3 = branch in headers.get('branch')
    if value1 and value2 and value3 == True:
        if roll_no.isdigit():
            return 'done!'
    return False
