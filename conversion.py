import docx2txt
import os

class Convert:


	def __init__(self, file_name = None):

		resume_no_data = r'C:\Users\Admin\PycharmProjects\web_apis\class_no_data'
		self.filename = file_name
		self.filePath = os.path.join(resume_no_data, self.filename)
		os.chdir(resume_no_data)

		if self.filename.endswith('.pdf'):
			self.pdf_to_text()

		if self.filename.endswith('.doc'):
			self.doc_to_text()

		if self.filename.endswith('.docx'):
			self.docx_to_text()


	def pdf_to_text(self):
		path = os.getcwd()
		self.new_filename = os.path.join(path, self.filename.replace(' ', '-'))
		if ' ' in self.filename:
			os.rename(self.filePath, self.new_filename)
		self.new_filePath = os.path.join(path, self.new_filename)
		os.system('pdftotext {0}'.format(self.new_filePath))

	def doc_to_text(self):
		path = os.getcwd()
		new_name = self.filename.split('.')[0] + '.txt'
		new_name = new_name.replace(' ','-')
		self.new_filename = os.path.join(path, self.filename.replace(' ', '-'))
		if ' ' in self.filename:
			os.rename(self.filePath, self.new_filename)
		self.new_filePath = os.path.join(path, self.new_filename)
		os.system('antiword {0} > {1}'.format(self.new_filePath, new_name))

	def docx_to_text(self):
		text = docx2txt.process(self.filePath)
		new_text = ''
		for char in text:
			if ord(char)>=127:
				continue
			else:
				new_text = new_text + char 
		new_file_name = self.filename.split('.')[0] + '.txt'
		new_file_name = new_file_name.replace(' ', '-')
		with open(new_file_name, 'w') as f:
			f.write(new_text)
			