import string
import pandas as pd
import re
df = pd.read_csv(r'C:\Users\Admin\PycharmProjects\web_apis\new_skills.csv', sep = ',', encoding = 'latin-1')
# print(df['Skills'])
# filepath = 'C:\pdftotext\\2017-04-13-08-10-22-NileshRaghunathPawar[4_0].txt'
skills = df.Skills.values

# punctuations = ["'", "!", '"', '$', '%', '(', ')', '*', ',', ':', ';', '<', '=', '>', '?', '@', '[', ']', '\\', '^', '_', '`', '{', '|', '}', '~' ] 
# Now read every individual single word of a text file and check if it exist in dataframe 'df' by df.Skills.values .
# Check the word in lower case.
# We can also write our own function to remove punctuation by making a list or string of punctuations and then modifying our existing string or making new strings.
# But use built-in function for efficiency purpose.
# To check if the list you get of skills is correct one find the index of that element in skills using "i, = np.where(skills == value)"
# Check also length, shape and type of 'skills' 
with open(r'C:\Users\Admin\PycharmProjects\web_apis\stopword.txt', encoding = 'latin-1') as f:
	file_read = f.read()
	#print(file_read)
def get_skills(filepath):
	skill_list = []
	with open(filepath, 'r', encoding='latin-1') as f:
		for line in f:   # Type of line is str
			for word in line.split(): # Type of word is str
				# print(word)
				words = word.split(',')
				for elem in words:
					elem = elem.lower()
					after_brack = re.sub('\(.*?\)|\(|\)','',elem)
					if '/' in after_brack:
						after_slash = after_brack.split('/')
						for el in after_slash:
							if el in skills and el not in file_read:
								skill_list.append(el)
					else:
						if after_brack in skills and after_brack not in file_read:
							skill_list.append(after_brack)


	my_skill_set = set(skill_list)
	my_unique_skill_list = list(my_skill_set)
	return my_unique_skill_list
		


#print(skill_list)
#print('\n')
# making unique list of skill_list
#my_skill_set = set(skill_list)
#my_unique_skill_list = list(my_skill_set)
#print(my_unique_skill_list)

