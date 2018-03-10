import os
from conversion import Convert
from email_id import get_email
from resume_data import Inside_Resume_Data
import time

class DownloadAttachment:

	def __init__(self, mailpart = None, filename = None):

		self.mailpart = mailpart
		self.filename = filename

	def resume_with_data(self):
		resume_data = r'C:\Users\Admin\PycharmProjects\web_apis\class_data'
		filePath = os.path.join(resume_data, self.filename)
		if not os.path.isfile(filePath):
			try:
				fp = open(filePath, 'wb')
				fp.write(self.mailpart.get_payload())
				fp.close()
			except:
				pass

	def resume_with_no_data(self):
		resume_no_data = r'C:\Users\Admin\PycharmProjects\web_apis\class_no_data'
		filePath = os.path.join(resume_no_data, self.filename)
		if not os.path.isfile(filePath):
			try:
				fp = open(filePath, 'wb')
				fp.write(self.mailpart.get_payload())
				fp.close()
			except:
				pass

	def change_name(self, url):
		Convert(self.filename)
		os.chdir(r'C:\Users\Admin\PycharmProjects\web_apis\class_no_data')
		for file in os.listdir():
			if file.endswith('.txt'):
				filePath = r'C:\Users\Admin\PycharmProjects\web_apis\class_no_data\\' + file
				try:
					candi_id, email = Inside_Resume_Data(filePath, url)
				except:
					continue
				email = get_email(filePath)
				bef_ext, after_ext = os.path.splitext(self.filename)
				new_name = '{}{}'.format(email, after_ext)
				try:
					os.rename(self.filename, new_name)
				except:
					pass

				os.remove(file)
				return candi_id, email, new_name
