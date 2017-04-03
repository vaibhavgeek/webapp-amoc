import sys
import requests
from BeautifulSoup import BeautifulSoup
data = {
	'mode':'191',
	'username':'i15ma007',
	'password':'now',
	'a':'1439199700564',
	'producttype':'0'
	}
send=requests.post('http://172.50.1.1:8090/login.xml',data=data).text
soup = BeautifulSoup(send)
if soup.message.string == "You have successfully logged in" or soup.message.string == "You have reached Maximum Login Limit.":
	print "true"
else:
	print "false"