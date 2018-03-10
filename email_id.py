import re
def get_email(text_file):
	with open(text_file, 'r', encoding = 'utf8', errors ='ignore' ) as f_txt:
		em_list = []
		for line in f_txt:
			em = re.compile(r'[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)')
			email_id = em.search(line)
			if email_id != None:
				# print(email_id)
				email_add = email_id.group()
				# print(email_add)
				em_list.append(email_add)
			#print(em_list)
		
	if len(em_list) != 0:
		return em_list[0]

	else:
		return "empty"