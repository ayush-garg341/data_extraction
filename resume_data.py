from extract_email_phone import read_email_phone
from extract_skill import get_skills
import json
import requests
import time
from get_token import gen_token
import os

def Inside_Resume_Data(filePath, url):

    phone_list, em_list = read_email_phone(filePath)
    skill_list = get_skills(filePath)
    skill_string = ', '.join(skill_list)
    if len(phone_list)!=0 and len(em_list)!=0:
        payload = {'address':'', 'candidateName':em_list[0], 'city':'', 'country':'99', 'currentDesignation':'', 'currentOrganization':'',
				'currentSalary':'', 'dob':'', 'email':em_list[0], 'expectedSalary':'', 'functionalArea':'', 'gender':'1', 'industryType':'',
				'skillSet':skill_string, 'location':'', 'mobileNo':phone_list[0], 'nationality':'', 'noticePeriod':'', 'ovarallExperiance':'', 
				'panNo':'', 'phoneNo':'', 'preferredLocation':'', 'qualification':'', 'relevantExperiance':'', 'remark':'',
				'source':'', 'state':'', 'visaType':''}
        res = requests.post(url, json=payload)
        candidate_id = res.json()
        time.sleep(5)
        return candidate_id['id'], em_list[0]

    else:
        os.chdir(r'C:\Users\Admin\PycharmProjects\web_apis\class_no_data')
        for files in os.listdir():
            os.remove(files)


	