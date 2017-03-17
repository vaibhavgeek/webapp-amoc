from flask import Flask
import os


app = Flask(__name__)




@app.route('/')
@app.route('/index')
def index():
	return "hello"

if __name__ == '__main__':
	app.secret_key = "unknown_cookie_values_present_here_so_that_it_remains_secret_so_dont worry_its still secret"
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)	
	