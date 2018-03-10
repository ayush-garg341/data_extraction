from ocr_dup import return_text
import json
import requests
import time
import re
import csv


def format_1(html_list, from_add, url):
	#print("format_1")
	try:
		name = from_add[0][0]
		#print(name)
		
		email = from_add[0][1]
		#print(email)
		
		for i in range(len(html_list)):
			skills = ''
			exp = ''
			ctc = ''
			location = ''
			curr_desig = ''
			curr_comp = ''
			notice = ''
			prev_desig = ''
			prev_comp = ''
			contact = ''
			mob = ''
			land_1 = ''
			pref_loc = ''
			edu = ''
			if 'Key Skills' in html_list[i]:
				skills = skills + html_list[i]
				count = i+1
				while 'Exp' not in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				skills = skills.replace('Key Skills', '')
				skills = skills.replace('|', '')
				skills = skills.replace('---', '')
				skills.strip()			
				#print('skills: ',skills)

				if 'Exp' in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1
				while 'CTC' not in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1
				exp = exp.replace('Exp','')
				exp = exp.replace('|', '')
				exp = exp.replace('---', '')
				exp.strip()
				#print('exp: ', exp)

				if 'CTC' in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1

				while 'Location' not in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1
				comp = re.compile(r'\(.*\)')
				ctc_group = comp.search(ctc)
				ctc = ctc_group.group()
				ctc = ctc.replace('(','')
				ctc = ctc.replace(')','')
				ctc_str = return_text(ctc)

				payload = {'currentSalary':ctc_str}
				#print('ctc: ',ctc_str)

				if 'Location' in html_list[count]:
					location = location + html_list[count]
					count = count + 1
				while 'Current Designation' not in html_list[count]:
					location = location + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*?\)')
				loc_group = comp.search(location)
				loc = loc_group.group()
				loc = loc.replace('(','')
				loc = loc.replace(')','')
				loc_str = return_text(loc)
				#print('Location:', loc_str)

				if 'Current Designation' in html_list[count]:
					curr_desig = curr_desig + html_list[count]
					count = count + 1

				while 'Current Company' not in html_list[count]:
					curr_desig = curr_desig + html_list[count]
					count = count + 1
				comp = re.compile(r'(\*\*.*\*\*)')
				curr_desig_group = comp.search(curr_desig)
				current_desig = curr_desig_group.group()
				current_desig = current_desig.replace('*','')

				payload = {'currentDesignation':current_desig}
				#print('Current Designation: ',current_desig)

				if 'Current Company' in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1
				while 'Notice Period' not in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1
				curr_comp = curr_comp.replace('Current Company', '')
				curr_comp.strip()

				payload = {'currentOrganization':curr_comp}
				#print('Current Company: ',curr_comp)

				if 'Notice Period' in html_list[count]:
					notice = notice + html_list[count]
					count = count + 1

				while 'Previous Designation' not in html_list[count]:
					notice = notice + html_list[count]
					count = count + 1
				notice = notice.replace('Notice Period', '')
				notice.strip()
				#print('Notice Period: ',notice)

				if 'Previous Designation' in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				while 'Previous Company' not in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				prev_desig = prev_desig.replace('Previous Designation','')
				#print('Previous Designation: ',prev_desig)

				if 'Previous Company' in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				while 'Contact Details' not in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				prev_comp = prev_comp.replace('Previous Company','')
				#print('Previous Company: ',prev_comp)

				if 'Contact Details' in html_list[count]:
					contact = contact + html_list[count]
					count = count + 1

				while 'Mobile' not in html_list[count]:
					contact = contact + html_list[count]
					count = count + 1

				if 'Mobile' in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				while 'Landline' not in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*\)')
				mob_group = comp.search(mob)
				mobile = mob_group.group()
				mobile = mobile.replace('(','')
				mobile = mobile.replace(')','')
				mobile_str = return_text(mobile)
				#print('Mobile: ',mobile_str)

				if 'Landline' in html_list[count]:
					land_1 = land_1 + html_list[count]
					count = count + 1

				while 'Prefers' not in html_list[count]:
					land_1 = land_1 + html_list[count]
					count = count + 1
				land_1 = land_1.replace('Landline:', '')
				land_1.strip()
				#print('Landline: ',land_1)

				if 'Prefers' in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				while 'Education' not in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				pref_loc = pref_loc.replace('|', '')
				pref_loc = pref_loc.replace('Prefers', '')
				pref_loc = pref_loc.replace('---', '')
				#print('Preferred Location: ',pref_loc)

				if 'Education' in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1

				while 'applicant relevant' not in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1
				edu = edu.replace('|','')
				edu = edu.replace('---','')
				edu = edu.replace('Education', '')
				edu.strip()
				#print('Education: ',edu)

				payload = {'address':'', 'candidateName':name, 'city':'', 'country':'99', 'currentDesignation':current_desig, 'currentOrganization':curr_comp,
				            'currentSalary':ctc_str, 'dob':'', 'email':email, 'expectedSalary':'', 'functionalArea':'', 'gender':'1', 'industryType':'',
				            'skillSet':skills, 'location':loc_str, 'mobileNo':mobile_str, 'nationality':'', 'noticePeriod':notice, 'ovarallExperiance':exp, 
				            'panNo':'', 'phoneNo':land_1, 'preferredLocation':pref_loc, 'qualification':edu, 'relevantExperiance':exp, 'remark':'',
				            'source':'', 'state':'', 'visaType':''}

				res = requests.post(url, json=payload)
				candidate_id = res.json()
				time.sleep(5)
				return candidate_id['id'], email 

	except:
		pass

def format_2(html_list, from_add, url):
	#print("format_2")
	try:
		name = from_add[0][0]
		#print(name)
		
		email = from_add[0][1]
		#print(email)
		
		for i in range(len(html_list)):
			skills = ''
			exp = ''
			ctc = ''
			location = ''
			curr_desig = ''
			curr_comp = ''
			notice = ''
			prev_desig = ''
			prev_comp = ''
			contact = ''
			mob = ''
			land_1 = ''
			pref_loc = ''
			edu = ''
			if 'Current Designation' in html_list[i]:
				curr_desig = curr_desig + html_list[i]
				count = i + 1

				while 'Current Company' not in html_list[count]:
					curr_desig = curr_desig + html_list[count]
					count = count + 1

				comp = re.compile(r'(\*\*.*\*\*)')
				curr_desig_group = comp.search(curr_desig)
				current_desig = curr_desig_group.group()

				current_desig = current_desig.replace('*','')
				#print('Current Designation: ',current_desig)

				if 'Current Company' in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1
				while 'Notice Period' not in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1
				curr_comp = curr_comp.replace('Current Company', '')
				curr_comp.strip()
				#print('Current Company: ',curr_comp)

				if 'Notice Period' in html_list[count]:
					notice = notice + html_list[count]
					count = count + 1

				while 'Previous Designation' not in html_list[count]:
					notice = notice + html_list[count]
					count = count + 1
				notice = notice.replace('Notice Period', '')
				notice.strip()
				#print('Notice Period: ',notice)

				if 'Previous Designation' in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				while 'Previous Company' not in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				prev_desig = prev_desig.replace('Previous Designation','')
				#print('Previous Designation: ',prev_desig)

				if 'Previous Company' in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				while 'Contact Details' not in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				prev_comp = prev_comp.replace('Previous Company','')
				#print('Previous Company: ',prev_comp)

				if 'Contact Details' in html_list[count]:
					contact = contact + html_list[count]
					count = count + 1

				while 'Mobile' not in html_list[count]:
					contact = contact + html_list[count]
					count = count + 1

				if 'Mobile' in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				while 'Landline' not in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*\)')
				mob_group = comp.search(mob)
				mobile = mob_group.group()
				mobile = mobile.replace('(','')
				mobile = mobile.replace(')','')
				mobile_str = return_text(mobile)
				#print('Mobile: ',mobile_str)

				if 'Landline' in html_list[count]:
					land_1 = land_1 + html_list[count]
					count = count + 1

				while 'Exp' not in html_list[count]:
					land_1 = land_1 + html_list[count]
					count = count + 1

				land_1 = land_1.replace('Landline:', '')
				land_1.strip()
				#print('Landline: ',land)

				if 'Exp' in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1
				while 'CTC' not in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1
				exp = exp.replace('Exp','')
				exp = exp.replace('|', '')
				exp = exp.replace('---', '')
				exp.strip()
				#print('exp: ', exp)

				if 'CTC' in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1

				while 'Location' not in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1
				comp = re.compile(r'\(.*\)')
				ctc_group = comp.search(ctc)
				ctc = ctc_group.group()
				ctc = ctc.replace('(','')
				ctc = ctc.replace(')','')
				ctc_str = return_text(ctc)
				#print('ctc: ',ctc_str)

				if 'Location' in html_list[count]:
					location = location + html_list[count]
					count = count + 1

				while 'Preferred Location' not in html_list[count]:
					location = location + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*?\)')
				loc_group = comp.search(location)
				loc = loc_group.group()
				loc = loc.replace('(','')
				loc = loc.replace(')','')
				loc_str = return_text(loc)
				#print('Location:', loc_str)

				if 'Preferred Location' in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				while 'Education' not in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				pref_loc = pref_loc.replace('|', '')
				pref_loc = pref_loc.replace('Preferred Location', '')
				pref_loc = pref_loc.replace('---', '')
				#print('Preferred Location: ',pref_loc)

				if 'Education' in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1

				while 'Key Skills' not in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1

				edu = edu.replace('|','')
				edu = edu.replace('---','')
				edu = edu.replace('Education', '')
				edu.strip()
				#print('Education: ',edu)

				if 'Key Skills' in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				while 'Screen candidates' not in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				skills = skills.replace('Key Skills', '')
				skills = skills.replace('|', '')
				skills = skills.replace('---', '')
				skills.strip()
			
				payload = {'address':'', 'candidateName':name, 'city':'', 'country':'99', 'currentDesignation':current_desig, 'currentOrganization':curr_comp,
				            'currentSalary':ctc_str, 'dob':'', 'email':email, 'expectedSalary':'', 'functionalArea':'', 'gender':'1', 'industryType':'',
				            'skillSet':skills, 'location':loc_str, 'mobileNo':mobile_str, 'nationality':'', 'noticePeriod':notice, 'ovarallExperiance':exp, 
				            'panNo':'', 'phoneNo':land_1, 'preferredLocation':pref_loc, 'qualification':edu, 'relevantExperiance':exp, 'remark':'',
				            'source':'', 'state':'', 'visaType':''}

				res = requests.post(url, json=payload)
				candidate_id = res.json()
				time.sleep(5)
				return candidate_id['id'], email

	except:
		pass

def format_3(html_list, from_add, url):
	#print("format_3")
	try:
		name = from_add[0][0]
		#print(name)
		
		email = from_add[0][1]
		#print(email)
		for i in range(len(html_list)):
			curr_desig = ''
			curr_comp = ''
			notice = ''
			prev_desig = ''
			prev_comp = ''
			contact = ''
			mob = ''
			exp = ''
			ctc = ''
			location = ''
			pref_loc = ''
			edu = ''
			skills = ''
			if 'Current Designation' in html_list[i]:
				curr_desig = curr_desig + html_list[i]
				count = i + 1

				while 'Current Company' not in html_list[count]:
					curr_desig = curr_desig + html_list[count]
					count = count + 1

				comp = re.compile(r'(\*\*.*\*\*)')
				curr_desig_group = comp.search(curr_desig)
				current_desig = curr_desig_group.group()
				current_desig = current_desig.replace('*','')
				#print('Current Designation: ',current_desig)

				if 'Current Company' in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1

				while 'Notice Period' not in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1

				curr_comp = curr_comp.replace('Current Company', '')
				curr_comp.strip()
				#print('Current Company: ',curr_comp)

				if 'Notice Period' in html_list[count]:
					notice = notice + html_list[count]
					count = count + 1

				while 'Previous Designation' not in html_list[count]:
					notice = notice + html_list[count]
					count = count + 1

				notice = notice.replace('Notice Period', '')
				notice.strip()
				#print('Notice Period: ',notice)

				if 'Previous Designation' in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				while 'Previous Company' not in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				prev_desig = prev_desig.replace('Previous Designation','')
				#print('Previous Designation: ',prev_desig)

				if 'Previous Company' in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				while 'Contact Details' not in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				prev_comp = prev_comp.replace('Previous Company','')
				#print('Previous Company: ',prev_comp)

				if 'Contact Details' in html_list[count]:
					contact = contact + html_list[count]
					count = count + 1

				while 'Mobile' not in html_list[count]:
					contact = contact + html_list[count]
					count = count + 1

				if 'Mobile' in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				while 'Exp' not in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*\)')
				mob_group = comp.search(mob)
				mobile = mob_group.group()
				mobile = mobile.replace('(','')
				mobile = mobile.replace(')','')
				mobile_str = return_text(mobile)

				if 'Exp' in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1

				while 'CTC' not in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1

				exp = exp.replace('Exp','')
				exp = exp.replace('|', '')
				exp = exp.replace('---', '')
				exp.strip()
				#print('exp: ', exp)

				if 'CTC' in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1

				while 'Location' not in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*\)')
				ctc_group = comp.search(ctc)
				ctc = ctc_group.group()
				ctc = ctc.replace('(','')
				ctc = ctc.replace(')','')
				ctc_str = return_text(ctc)
				#print('ctc: ',ctc_str)

				if 'Location' in html_list[count]:
					location = location + html_list[count]
					count = count + 1

				while 'Preferred Location' not in html_list[count]:
					location = location + html_list[count]
					count = count + 1

				comp = re.compile(r'\(.*?\)')
				loc_group = comp.search(location)
				loc = loc_group.group()
				loc = loc.replace('(','')
				loc = loc.replace(')','')
				loc_str = return_text(loc)
				#print('Location:', loc_str)

				if 'Preferred Location' in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				while 'Education' not in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				pref_loc = pref_loc.replace('|', '')
				pref_loc = pref_loc.replace('Preferred Location', '')
				pref_loc = pref_loc.replace('---', '')
				#print('Preferred Location: ',pref_loc)

				if 'Education' in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1

				while 'Key Skills' not in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1

				edu = edu.replace('|','')
				edu = edu.replace('---','')
				edu = edu.replace('Education', '')
				edu.strip()
				#print('Education: ',edu)

				if 'Key Skills' in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				while 'Shortlist' not in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				skills = skills.replace('Key Skills', '')
				skills = skills.replace('|', '')
				skills = skills.replace('---', '')
				skills.strip()

				payload = {'address':'', 'candidateName':name, 'city':'', 'country':'99', 'currentDesignation':current_desig, 'currentOrganization':curr_comp,
				            'currentSalary':ctc_str, 'dob':'', 'email':email, 'expectedSalary':'', 'functionalArea':'', 'gender':'1', 'industryType':'',
				            'skillSet':skills, 'location':loc_str, 'mobileNo':mobile_str, 'nationality':'', 'noticePeriod':notice, 'ovarallExperiance':exp, 
				            'panNo':'', 'phoneNo':land_1, 'preferredLocation':pref_loc, 'qualification':edu, 'relevantExperiance':exp, 'remark':'',
				            'source':'', 'state':'', 'visaType':''}

				res = requests.post(url, json=payload)
				candidate_id = res.json()
				time.sleep(5)
				return candidate_id['id'], email
				
	except:
		pass

def format_4(html_list, from_add, url):
	
	try:
		email = from_add[0][1]
		print(email)
		for i in range(len(html_list)):
			if 'Resume Headline' in html_list[i]:
				comp = re.compile(r'\:(.*)*')
				res_title_group = comp.search(html_list[i])
				res_title = res_title_group.group()
				count = i + 1

				while 'Key Skills' not in html_list[count]:
					res_title = res_title + html_list[count]
					count = count + 1

				res_title = res_title.replace(':', '')
				res_title = res_title.replace('|', '')
				print(res_title)

				if 'Key Skills' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					skills_group = comp.search(html_list[count])
					skills = skills_group.group()
				count = count + 1

				while 'Name' not in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				skills = skills.replace(':', '')
				skills = skills.replace('|', '')
				#print(skills)

				if 'Name' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					name_group = comp.search(html_list[count])
					name = name_group.group()

				count = count + 1
				while 'Total Experience' not in html_list[count]:
					name = name + html_list[count]
					count = count + 1

				name = name.replace(':', '')
				name = name.replace('|', '')
				#print(name)

				if 'Total Experience' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					exp_group = comp.search(html_list[count])
					exp = exp_group.group()

				count = count + 1

				while 'CTC' not in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1

				exp = exp.replace(':', '')
				exp = exp.replace('|', '')
				#print(exp)

				if 'CTC' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					ctc_group = comp.search(html_list[count])
					ctc = ctc_group.group()

				count = count + 1

				while 'Current Employer' not in html_list[count]:
					ctc = ctc + html_list[count]
					count = count + 1

				ctc = ctc.replace(':', '')
				ctc = ctc.replace('|', '')
				#print(ctc)

				if 'Current Employer' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					curr_comp_group = comp.search(html_list[count])
					curr_comp = curr_comp_group.group()

				count = count + 1

				while 'Current Designation' not in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1

				curr_comp = curr_comp.replace(':', '')
				curr_comp = curr_comp.replace('|', '')
				#print(curr_comp)

				if 'Current Designation' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					curr_desig_group = comp.search(html_list[count])
					curr_desig = curr_desig_group.group()

				count = count +1

				while 'Last Employer' not in html_list[count]:
					curr_desig = curr_desig + html_list[count]
					count = count + 1

				curr_desig = curr_desig.replace(':', '')
				curr_desig = curr_desig.replace('|', '')
				#print(curr_desig)

				if 'Last Employer' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					prev_comp_group = comp.search(html_list[count])
					prev_comp = prev_comp_group.group()
				count = count + 1

				while 'Last Designation' not in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				prev_comp = prev_comp.replace(':', '')
				prev_comp = prev_comp.replace('|', '')
				#print(prev_comp)

				if 'Last Designation' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					prev_desig_group = comp.search(html_list[count])
					prev_desig = prev_desig_group.group()

				count = count + 1
				while 'Current Location' not in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				prev_desig = prev_desig.replace(':', '')
				prev_desig = prev_desig.replace('|', '')
				#print(prev_desig)

				if 'Current Location' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					curr_loc_group = comp.search(html_list[count])
					curr_loc = curr_loc_group.group()
				count = count + 1

				while 'Preferred Location' not in html_list[count]:
					curr_loc = curr_loc + html_list[count]
					count = count + 1

				curr_loc = curr_loc.replace(':', '')
				curr_loc = curr_loc.replace('|', '')
				#print(curr_loc)

				if 'Preferred Location' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					pref_loc_group = comp.search(html_list[count])
					pref_loc = pref_loc_group.group()

				count = count + 1

				while 'Education' not in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1

				pref_loc = pref_loc.replace(':', '')
				pref_loc = pref_loc.replace('|', '')
				#print(pref_loc)

				if 'Education' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					edu_group = comp.search(html_list[count])
					edu = edu_group.group()

				count = count + 1
				while 'Mobile' not in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1
				edu = edu.replace(':', '')
				edu = edu.replace('|', '')
				#print(edu)

				if 'Mobile' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					mob_group = comp.search(html_list[count])
					mob = mob_group.group()

				count = count + 1
				while 'Landline' not in html_list[count]:
					mob = mob + html_list[count]
					count = count + 1

				mob = mob.replace(':', '')
				mob = mob.replace('|', '')
				#print(mob)
				if 'Landline' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					land_group = comp.search(html_list[count])
					land = land_group.group()

				count = count + 1

				while 'Recommendations' not in html_list[count]:
					land = land + html_list[count]
					count = count + 1

				land = land.replace(':', '')
				land = land.replace('|', '')
				#print(land)
				if 'Recommendations' in html_list[count]:
					comp = re.compile(r'\:(.*)*')
					recom_group = comp.search(html_list[count])
					recom = recom_group.group()
				count = count + 1
				while 'Last modified on' not in html_list[count]:
					recom = recom + html_list[count]
					count = count + 1

					


				payload = {'address':'', 'candidateName':name, 'city':'', 'country':'99', 'currentDesignation':curr_desig, 'currentOrganization':curr_comp,
					            'currentSalary':ctc, 'dob':'', 'email':email, 'expectedSalary':'', 'functionalArea':'', 'gender':'1', 'industryType':'',
					            'skillSet':skills, 'location':curr_loc, 'mobileNo':mob, 'nationality':'', 'noticePeriod':'', 'ovarallExperiance':exp, 
					            'panNo':'', 'phoneNo':land_1, 'preferredLocation':pref_loc, 'qualification':edu, 'relevantExperiance':exp, 'remark':'',
					            'source':'', 'state':'', 'visaType':''}

				res = requests.post(url, json=payload)
				candidate_id = res.json()
				time.sleep(5)
				return candidate_id['id'], email

	except:
		pass

def format_5(html_list, from_add, url):

	try:
		email = from_add[0][1]
		#print(email)
		for i in range(len(html_list)):
			if 'Current Designation:' in html_list[i]:
				comp = re.compile(r'\*\*.*\*\*')
				count_prev = i-1
				while not comp.search(html_list[count_prev]):
					count_prev = count_prev-1

				name_group = comp.search(html_list[count_prev])
				name = name_group.group()
				name = name.replace('*', '')
				#print(name)

				comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
				curr_desig_group = comp.search(html_list[i])
				curr_desig = curr_desig_group.group()

				count = i + 1
				while 'Current Company:' not in html_list[count]:
					curr_desig = curr_desig + html_list[count]
					count = count + 1

				curr_desig = curr_desig.replace(':', '')
				curr_desig = curr_desig.replace('*', '')
				curr_desig = curr_desig.replace('-', '')
				#print(curr_desig)

				if 'Current Company:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					curr_comp_group = comp.search(html_list[count])
					curr_comp = curr_comp_group.group()

				count = count + 1

				while 'Previous Designation:' not in html_list[count]:
					curr_comp = curr_comp + html_list[count]
					count = count + 1

				curr_comp = curr_comp.replace(':', '')
				curr_comp = curr_comp.replace('*', '')
				#print(curr_comp)

				if 'Previous Designation:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					prev_desig_group = comp.search(html_list[count])
					prev_desig = prev_desig_group.group()

				count = count + 1

				while 'Previous Company:' not in html_list[count]:
					prev_desig = prev_desig + html_list[count]
					count = count + 1

				prev_desig = prev_desig.replace(':', '')
				prev_desig = prev_desig.strip()
				#print(prev_desig)

				if 'Previous Company:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					prev_comp_group = comp.search(html_list[count])
					prev_comp = prev_comp_group.group()
				count = count + 1

				while 'Current Location:' not in html_list[count]:
					prev_comp = prev_comp + html_list[count]
					count = count + 1

				prev_comp = prev_comp.replace(':', '')
				prev_comp = prev_comp.strip()

				#print(prev_comp)
				if 'Current Location:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					curr_loc_group = comp.search(html_list[count])
					curr_loc = curr_loc_group.group()

				count = count + 1

				while 'Exp:' not in html_list[count]:
					curr_loc = curr_loc + html_list[count]
					count = count + 1

				curr_loc = curr_loc.replace(':', '')
				curr_loc = curr_loc.replace('*', '')
				curr_loc = curr_loc.replace('-', '')
				#print(curr_loc)

				if 'Exp:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\(\)\/]*')
					exp_group = comp.search(html_list[count])
					exp = exp_group.group()

				count = count + 1
				while 'CTC:' not in html_list[count]:
					exp = exp + html_list[count]
					count = count + 1

				exp = exp.replace(':', '')
				exp = exp.replace('*', '')
				exp = exp.replace('-', '')
				#print(exp)

				if 'CTC:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					ctc_group = comp.search(html_list[count])
					ctc = ctc_group.group()
					ctc = ctc.replace('*', '')
				count = count + 1
				edu = ''
				while 'Pref Location:' not in html_list[count]:
					edu = edu + html_list[count]
					count = count + 1

				edu = edu.replace(':', '')
				edu = edu.strip()
				#print(edu)

				if 'Pref Location' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					pref_loc_group = comp.search(html_list[count])
					pref_loc = pref_loc_group.group()

				count = count + 1

				while 'Key Skills:' not in html_list[count]:
					pref_loc = pref_loc + html_list[count]
					count = count + 1
				pref_loc = pref_loc.replace(':', '')
				pref_loc = pref_loc.strip()
				#print(pref_loc)
				if 'Key Skills:' in html_list[count]:
					comp = re.compile(r'\:[A-Za-z0-9\.\s\*\-\,\&\/]*')
					skills_group = comp.search(html_list[count])
					skills = skills_group.group()

				count = count + 1
				while '*' not in html_list[count]:
					skills = skills + html_list[count]
					count = count + 1

				skills = skills.replace(':', '')
				skills = skills.strip()
				#print(skills)
				

				payload = {'address':'', 'candidateName':name, 'city':'', 'country':'99', 'currentDesignation':curr_desig, 'currentOrganization':curr_comp,
					            'currentSalary':ctc, 'dob':'', 'email':email, 'expectedSalary':'', 'functionalArea':'', 'gender':'1', 'industryType':'',
					            'skillSet':skills, 'location':curr_loc, 'mobileNo':'', 'nationality':'', 'noticePeriod':'', 'ovarallExperiance':exp, 
					            'panNo':'', 'phoneNo':land_1, 'preferredLocation':pref_loc, 'qualification':'', 'relevantExperiance':exp, 'remark':'',
					            'source':'', 'state':'', 'visaType':''}

				res = requests.post(url, json=payload)
				candidate_id = res.json()
				time.sleep(5)
				return candidate_id['id'], email

	except:
		pass

