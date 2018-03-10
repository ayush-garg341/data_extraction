import html2text, pprint, pyzmail
import sys, os
from nltk import word_tokenize
import re
from make_connection import EstablishConnection
from datetime import date
from sending_data_api import format_1, format_2, format_3, format_4, format_5
from renaming_resumes import DownloadAttachment
from send_resume_api import SendResume
from get_token import gen_token
import time

class ExtractData:

	def __init__(self, mail_server, port, ssl_enabling, user_name, password, token=None):

		if token!=None:
			self.token=token

		try:
			self.mail_ids, self.conn = EstablishConnection(mail_server, port, ssl_enabling, user_name, password).check_connection()
		except:
			print("Invalid Details\n")
		
		self.data_post_url = 'http://api.passivereferral.com/index.php/api/candidatedetail/?token=' + self.token

	def convert_into_html(self):
		for i in self.mail_ids[:]:
			rawMessages = self.conn.fetch(i, ['BODY[]', 'FLAGS'])
			message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
			sub_mess = self.mess_subject(message)
			from_add = self.mess_address(message)
			if message.text_part != None:
				try:
					html_text = message.text_part.get_payload().decode(message.text_part.charset)
					html_list = html_text.split('\n')
				except:
					continue

			elif message.html_part != None:
				try:
					html_text = html2text.html2text(message.html_part.get_payload().decode(message.html_part.charset))
					html_list = html_text.split('\n')
				except:
					continue

			list_join = ''.join(html_list)

			if ('Key Skills' in list_join and 'Exp' in list_join and 'CTC' in list_join and 'Location' in list_join and 'Current Designation' in list_join and 'Current Company' in list_join and 'Notice Period' in list_join and 'Previous Designation' in list_join and 'Previous Company' in list_join and 'Contact Details' in list_join and 'Mobile' in list_join and 'Landline' in list_join and 'Prefers' in list_join and 'Education' in list_join and 'applicant relevant' in list_join):
				can_id, email = format_1(html_list, from_add, self.data_post_url)
				url = 'http://api.passivereferral.com/index.php/api/uploadresume/' + str(can_id) +'?token='+ self.token + '&email=' + email
				for mailpart in message.mailparts:
					if mailpart.filename != None:
						fileName = self.check_attachment(mailpart)
						SendResume().send_file_with_data(url, fileName)



			elif ('Current Designation' in list_join and 'Current Company' in list_join and 'Notice Period' in list_join and 'Previous Designation' in list_join and 'Previous Company'
                in list_join and 'Contact Details' in list_join and 'Mobile' in list_join and 'Landline' in list_join and 'Exp' in list_join and 'CTC' in list_join and 'Location' in 
                list_join and 'Preferred Location' in list_join and 'Education' in list_join and 'Key Skills' in list_join and 'Screen candidates' in list_join):
				can_id, email = format_2(html_list, from_add, self.data_post_url)
				url = 'http://api.passivereferral.com/index.php/api/uploadresume/' + str(can_id) +'?token='+ self.token + '&email=' + email
				for mailpart in message.mailparts:
					if mailpart.filename != None:
						fileName = self.check_attachment(mailpart)
						SendResume().send_file_with_data(url, fileName)


			elif ('Current Designation' in list_join and 'Current Company' in list_join and 'Notice Period' in list_join and 'Previous Designation' in list_join and 'Previous Company' in 
                list_join and 'Contact Details' in list_join and 'Mobile' in list_join and 'Exp' in list_join and 'CTC' in list_join and 'Location' in list_join and 'Preferred Location' in
                list_join and 'Education' in list_join and 'Key Skills' in list_join and 'Shortlist' in list_join ):
				can_id, email = format_3(html_list, from_add, self.data_post_url)
				url = 'http://api.passivereferral.com/index.php/api/uploadresume/' + str(can_id) +'?token='+ self.token + '&email=' + email
				for mailpart in message.mailparts:
					if mailpart.filename != None:
						fileName = self.check_attachment(mailpart)
						SendResume().send_file_with_data(url, fileName)

			elif ('Resume Headline' in list_join and 'Key Skills' in list_join and 'Name' in list_join and 'Total Experience' in list_join and 'CTC' in 
                list_join and 'Current Employer' in list_join and 'Current Designation' in list_join and 'Last Employer' in list_join and 'CTC' in list_join and 'Last Designation' in list_join and 'Current Location' in
                list_join and 'Preferred Location' in list_join and 'Education' in list_join and 'Mobile' in list_join and 'Landline' in list_join and 'Recommendations' in list_join and 'Last modified on' in list_join) or ('Naukri.com' in sub_mess):
				can_id, email = format_4(html_list, from_add, self.data_post_url)
				url = 'http://api.passivereferral.com/index.php/api/uploadresume/' + str(can_id) +'?token='+ self.token + '&email=' + email
				for mailpart in message.mailparts:
					if mailpart.filename != None:
						fileName = self.check_attachment(mailpart)
						SendResume().send_file_with_data(url, fileName)

			elif ('Current Designation:' in list_join and 'Current Company:' in list_join and 'Previous Designation:' in list_join and 'Previous Company:' in list_join and 'Current Location:' in 
                list_join and 'Exp:' in list_join and 'CTC:' in list_join and 'Pref Location:' in list_join and 'Key Skills:' in list_join) or ('found matching search' in sub_mess or 'Resumes Matching' in sub_mess):
				can_id, email = format_5(html_list, from_add, self.data_post_url)
				url = 'http://api.passivereferral.com/index.php/api/uploadresume/' + str(can_id) +'?token='+ self.token + '&email=' + email
				for mailpart in message.mailparts:
					if mailpart.filename != None:
						fileName = self.check_attachment(mailpart)
						SendResume().send_file_with_data(url, fileName)

			else:
				for mailpart in message.mailparts:
					if mailpart.filename != None:
						file_name = ''
						file_name = file_name + mailpart.filename
						if bool(file_name):
							if file_name.endswith('pdf') or file_name.endswith('docx') or file_name.endswith('doc') or file_name.endswith('DOC') or file_name.endswith('DOCX'):
								x = DownloadAttachment(mailpart, file_name)
								x.resume_with_no_data()

						try:
							can_id, email, new_name = x.change_name(self.data_post_url)
						except:
							continue
						url = 'http://api.passivereferral.com/index.php/api/uploadresume/' + str(can_id) +'?token='+ self.token + '&email=' + email
						SendResume().send_file_with_no_data(url, new_name)
						
	def mess_subject(self, message):
		return message.get_subject()

	def mess_address(self, message):
		return message.get_addresses('from')

	def check_attachment(self, mailpart):
		file_name = ''
		file_name = file_name + mailpart.filename
		if bool(file_name):
			if file_name.endswith('pdf') or file_name.endswith('docx') or file_name.endswith('doc') or file_name.endswith('DOC') or file_name.endswith('DOCX'):
				x = DownloadAttachment(mailpart, file_name).resume_with_data()
				return file_name