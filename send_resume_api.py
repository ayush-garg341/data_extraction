import json
import requests
import time
import os
class SendResume:

	def __init__(self):

		self.resume_data = r'C:\Users\Admin\PycharmProjects\web_apis\class_data'
		self.resume_no_data = r'C:\Users\Admin\PycharmProjects\web_apis\class_no_data'

	def send_file_with_data(self, url, filename):
		os.chdir(self.resume_data)

		for f in os.listdir():
			if f == filename:
				file_path = self.resume_data + '\\' + f
				fi = {'file': open(file_path, 'rb')}
				res = requests.post(url, files=fi)
				time.sleep(5)
			else:
				os.remove(f)

	def send_file_with_no_data(self, resume_url, filename):
		os.chdir(self.resume_no_data)
		for f in os.listdir():
			if f == filename:
				file_path = self.resume_no_data + '\\' + f
				fi = {'file': open(file_path, 'rb')}
				res = requests.post(resume_url, files=fi)
				print(True)
				time.sleep(5)
			else:
				os.remove(f)