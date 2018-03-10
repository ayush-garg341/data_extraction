import re
import json
import requests

def gen_token():
	payload = {'email':'gargayush341@gmail.com', 'password':'admin123'}
	res = requests.post('http://api.passivereferral.com/index.php/api/authenticate/', json=payload)
	#print(res.json())
	tok = res.json()
	#print(type(tok))
	return tok['token']
#x = res.content
#print(x)
#print(type(x))
#y = str(x)
#print(type(y))
#comp = re.compile(r'(":.*")')
#token_gr = comp.search(y)
#token = token_gr.group()
#token = token.replace('"','')
#token = token.replace(':','')
#print(token)
#print(type(token))
#print(x[3])
#print(chr(x[3]))
#print(res.status_code)