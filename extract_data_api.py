from flask import Flask,request
from flask_cors import CORS, cross_origin
from smtp_details import details

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return 'Ayush Garg'

@app.route('/extract_data/<string:check>')
@cross_origin()
def run(check):
	sec_check = '32kllk234u32lk34lk4553535333'
	if check == sec_check:
		details()
		return 'completed run'

	else:
		return 'somthing went wrong'

if __name__=="__main__":
	app.run(host = '0.0.0.0', debug = True)
