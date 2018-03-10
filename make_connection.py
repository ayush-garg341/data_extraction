import imapclient
from backports import ssl
from datetime import date
import pyzmail
import csv
from datetime import date, timedelta
import email.utils
import pandas as pd

class EstablishConnection:

	def __init__(self, mail_server = None, port = None, ssl_enabled = False, user_name = None, password = None):
		""" date:- Parameter from which you want data extraction
			format =  date(2018,1,11) i.e. (year, month, date)"""

		self.server = mail_server
		if self.server == None:
			self.server = 'mail.passivereferral.com'
		
		self.port = port
		if self.port == None:
			self.port = 143
		
		self.ssl = ssl_enabled

		self.user_name = user_name
		if self.user_name == None:
			self.user_name = 'amar.k@passivereferral.com'

		self.password = password
		if self.password == None:
			self.password = 'amar123'

		self.filename = r"C:\Users\Admin\PycharmProjects\web_apis\email_logs.csv"


	def check_connection(self):

		if self.server == 'imap.gmail.com' or self.server == 'imap.googlemail.com':
			return self.gmail_connection()

		elif self.ssl == False:
			return self.not_ssl_connection()

		elif ( self.ssl == True ) and ( self.server != 'imap.gmail.com' or self.server != 'imap.googlemail.com' ):
			return self.ssl_connection()


	def gmail_connection(self):
		context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
		context.verify_mode = ssl.CERT_NONE
		context.check_hostname = False
		self.conn = imapclient.IMAPClient('imap.googlemail.com', ssl=True, ssl_context = context)
		return self.form_csv()
		

	def not_ssl_connection(self):
		self.conn = imapclient.IMAPClient(self.server, use_uid=True, ssl=False)
		return self.form_csv()
		

	def ssl_connection(self):
		context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
		context.verify_mode = ssl.CERT_NONE
		context.check_hostname = False
		self.conn = imapclient.IMAPClient(self.server, port = self.port, ssl=True, ssl_context = context)
		return self.form_csv()


	def form_csv(self):
		self.conn.login(self.user_name, self.password)
		self.conn.select_folder('INBOX', readonly=True)
		df = pd.read_csv(self.filename)
		em_list = list(df['email'])
		if self.user_name not in em_list:
			all_UIDs = self.conn.search([u'ALL'])
			first_uid = all_UIDs[0]
			rawMessages = self.conn.fetch(first_uid, ['BODY[]', 'FLAGS'])
			message = pyzmail.PyzMessage.factory(rawMessages[first_uid][b'BODY[]'])
			start_date = message.get_decoded_header('date', '')
			start_date = email.utils.parsedate(start_date)
			start_date = date(start_date[0], start_date[1], start_date[2])
			end_date = start_date + timedelta(days = 2)
			with open(self.filename, 'a', newline = '') as csvfile:
				fieldnames = ['email', 'password', 'date']
				writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
				writer.writerow({'email':self.user_name, 'password':self.password, 'date':end_date})
			UIDs = self.conn.search([u'SINCE', start_date, u'BEFORE', end_date])
			return UIDs, self.conn

		else:
			file = open(self.filename)
			reader = csv.reader(file)
			for row in reader:
				if row[0] == self.user_name:
					try:
						year = int(row[2].split('-')[0])
					except:
						year = int(row[2].split('/')[2])
					try:
						month = int(row[2].split('-')[1])
					except:
						month = int(row[2].split('/')[0])
					try:
						day = int(row[2].split('-')[2])
					except:
						day = int(row[2].split('/')[1])
					start_date = date(year, month, day)
					end_date = start_date + timedelta(days = 2)
					write_df = pd.read_csv(self.filename)
					write_df.loc[write_df["email"]==self.user_name, "date"] = end_date
					write_df.to_csv(self.filename, index = False)
					UIDs = self.conn.search([u'SINCE', start_date, u'BEFORE', end_date])
					return UIDs, self.conn