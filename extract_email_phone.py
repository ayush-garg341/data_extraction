import os
import csv
import re
import string

def read_email_phone(file_path):
    l =[]
    with open(file_path, 'r', encoding = 'utf8', errors ='ignore' ) as f:
        #print(file_path)
        phone_list = []
        em_list = []
        for line in f:
            # print(line)
            phone = re.compile(r'\d{10,12}')
            mo = phone.search(line)
            if mo!= None:
                phone_number = mo.group()
                phone_list.append(phone_number)
                # print(phone_number)
                for i in range(len(phone_list)):
                    if len(phone_list[i]) == 12:
                        phone_list[i] = phone_list[i][2:]
                    if len(phone_list[i]) == 11:
                        phone_list[i] = phone_list[i][1:]
                # print(phone_list)

            if len(phone_list)==0:
                phone = re.compile(r'\d{5}\s\d{5}|\d{3}\s\d{3}\s\d{4}|\d{4}\s\d{3}\s\d{3}|\d{3}-\d{3}-\d{4}|\d{4}-\d{3}-\d{3}|\d{2}\s\d{2}\s\d{6}')
                mo = phone.search(line)
                if mo != None:
                    phone_number = mo.group()
                    s = "".join((char for char in phone_number if char not in string.punctuation))
                    phone_list.append(s)


                    # print(phone_list)
            
            
            em = re.compile(r'[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)')
            email_id = em.search(line)
            if email_id != None:
                # print(email_id)
                email_add = email_id.group()
                # print(email_add)
                em_list.append(email_add)
                # print(em_list)
            
                # print(email_add)
    return phone_list, em_list
    
''' This program will simply open a csv file and append a header to it.'''
#with open('data.csv', 'w', newline = '') as csvfile:
#    fieldnames = ['mobile_num', 'email']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    for files in os.listdir(txtDir):
#        file_path = txtDir + '\\' + files
#        phone_list, em_list = write_data(file_path)
#        phone_list_unique = []
#        em_list_unique = []
#        if len(phone_list) != 0:
#            for i in range(len(phone_list)):
#                if phone_list[i] not in phone_list_unique:
#                    phone_list_unique.append(phone_list[i])

#        if len(em_list) != 0:
#            for i in range(len(em_list)):
#                if em_list[i] not in em_list_unique:
#                    em_list_unique.append(em_list[i])

#        if len(phone_list_unique) == 0 and len(em_list_unique) != 0:
#            writer.writerow({'mobile_num': 'Not available', 'email': em_list_unique[:]})

#        if len(phone_list_unique) != 0 and len(em_list_unique) == 0:
#            writer.writerow({'mobile_num': phone_list_unique[:], 'email': 'Not available'})

#        if len(phone_list_unique) == 0 and len(em_list_unique) == 0:
#            writer.writerow({'mobile_num': 'Not available', 'email': 'Not available'})

#        if len(phone_list_unique) != 0 and len(em_list_unique) != 0:
#            writer.writerow({'mobile_num': phone_list_unique[:], 'email': em_list_unique[:]})

        
#csvfile.close()
