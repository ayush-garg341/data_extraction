import pymysql
import nltk
from get_skills_modify import return_skills

def jd_skills(jd):
    if len(jd) == 0:
        db = pymysql.connect("localhost","root","","pr111" )
        cursor = db.cursor()
        sql = "Select * from pr111.add_new_jobs"
        cursor.execute(sql)
        results = cursor.fetchall()


        # For selecting a particular jobDescription
        for result in results:
            if result[0] == 13:
                jd_data = result[6]

        #print(jd_data)
        # For removing the special characters which we use in word.
        jd_data_str = ''
        for char in jd_data:
            if ord(char)>127:
                continue

            else:
                jd_data_str = jd_data_str + char


        # remove the punctuation which can't be removed by the use of NLTK like '/'.
        if '/' in jd_data_str:
            jd_data_str = jd_data_str.replace('/', ' ')


        # Now using nltk to clean the data and getting the desired result
        jd_words = nltk.word_tokenize(jd_data_str)
        jd_tags = nltk.pos_tag(jd_words)


        # Selecting skills from the jd
        jd_skills = []
        for i, (word, tag) in enumerate(jd_tags):
            s = ''  # for getting the word like 'cloud computing'
            if tag == "NNP":
                jd_skills.append(word)
                if i != len(jd_tags)-1 and jd_tags[i+1][1] == 'VBG' :
                    jd_skills.pop()
                    s = jd_tags[i][0] + ' ' + jd_tags[i+1][0]
                    jd_skills.append(s)


        jd_skills_set = set(jd_skills)
        jd_skills_list = list(jd_skills_set)
        #print('Originally recommended skills by NLP : ',jd_skills_list)

        suggested_list = []
        for skill in jd_skills_list:
            suggested_list.append(skill.lower())
            a = return_skills(skill.lower())
            if a == '':
                continue
            else:
                for skill in a:
                    if skill not in suggested_list:
                        suggested_list.append(skill)

        return (suggested_list)

    else:
        jd_data_str = ''
        for char in jd:
            if ord(char)>127:
                continue

            else:
                jd_data_str = jd_data_str + char


        # remove the punctuation which can't be removed by the use of NLTK like '/'.
        if '/' in jd_data_str:
            jd_data_str = jd_data_str.replace('/', ' ')


        # Now using nltk to clean the data and getting the desired result
        jd_words = nltk.word_tokenize(jd_data_str)
        jd_tags = nltk.pos_tag(jd_words)


        # Selecting skills from the jd
        jd_skills = []
        for i, (word, tag) in enumerate(jd_tags):
            s = ''  # for getting the word like 'cloud computing'
            if tag == "NNP":
                jd_skills.append(word)
                if i != len(jd_tags)-1 and jd_tags[i+1][1] == 'VBG' :
                    jd_skills.pop()
                    s = jd_tags[i][0] + ' ' + jd_tags[i+1][0]
                    jd_skills.append(s)


        jd_skills_set = set(jd_skills)
        jd_skills_list = list(jd_skills_set)
        #print('Originally recommended skills by NLP : ',jd_skills_list)

        suggested_list = []
        for skill in jd_skills_list:
            suggested_list.append(skill.lower())
            a = return_skills(skill.lower())
            if a == '':
                continue
            else:
                for skill in a:
                    if skill not in suggested_list:
                        suggested_list.append(skill)

        with open(r'C:\Users\Admin\PycharmProjects\web_apis\unique_skill_set.csv') as f:
            s = [ line.replace('\n', '') for line in f]
            print(s)
        final_list = []
        for skill in suggested_list:
            if skill in s:
                final_list.append(skill)
        return final_list

