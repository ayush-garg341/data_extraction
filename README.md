# data_extraction
These are the python files to extract data in specified formats from emails sent by naukri.com and send the extracted data to the database.<br />
**conversion.py** :- convert pdf, docx and doc to simply text files.<br />
**email_id.py** :- to extract email-id from the corresponding text files to rename the resumes uniquely.<br />
**extract_data.py** :- make connection to mail server and extract data from the specified formats.<br />
**extract_data_api.py** :- flask api so that my program runs everytime it is hit with a particular url<br />
**extract_email_phone.py** :- to extract email and phone<br />
**extract_skill.py** :- this is to extract skill from the corresponding conversion of resume file with already made skill list.<br />
**make_connection.py** :- this is to establish connection with different mail servers.<br />
**ocr_dup.py** :- this file is intended to extract the data from the images as some email contains data which has images of mobile num, ctc, location.<br />
**renaming_resumes** :- this file rename the resume based on email-id extracted from the resume so to rename them uniquely.<br />
**send_resume_api.py** :- this is to send the renamed resume to the database.<br />
**sending_data_api.py** :- this contains the logic of extracting the details from the emails sent by Naukri.com in specified format.<br />
**smtp_details.py** :- this file extract the mail server details and establish a connection accordingly, little incomplete and still to do some work.<br />
