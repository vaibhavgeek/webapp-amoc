from flask import Flask
import os
from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import requests
from BeautifulSoup import BeautifulSoup
app = Flask(__name__)

engine = create_engine('sqlite:///amoc.db')

@app.route('/')
@app.route('/index')
def index():
	return "hello"

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
	