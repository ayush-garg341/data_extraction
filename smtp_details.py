import json
import requests
from extract_data import ExtractData

def details():
	payload = {'email':'arvind.chaudhary@passivereferral.com', 'password':'arvind123'}
	res_1 = requests.post('http://api.passivereferral.com/index.php/api/authenticate/', json=payload)
	tok = res_1.json()
	token = tok['token']
	url = r'http://api.passivereferral.com/index.php/api/getsmtp/?token=' + token
	res = requests.get(url, json=payload)
	response = res.json()[0] 
	user_name = response['user_name']
	password = response['password']
	mail_server = response['smtpname']
	ssl_enabling = response['ssl_enabled']
	token = response['token']
	if ssl_enabling == '0':
		port = None
		y = ExtractData(mail_server, None , False , user_name, password, token)
		y.convert_into_html()
