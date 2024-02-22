import json
import pandas as pd
from pprint import pprint


df = pd.read_excel('ключ оценка 360.xlsx', sheet_name='данные')

list_of_questions = [line[0] for num, line in enumerate(df.values.tolist()) if str(line[0]) != 'nan']

df = pd.read_excel('ключ оценка 360.xlsx', sheet_name='Ключ')

# print(*df.values.tolist(), sep='\n')
structure = {}
group_name = ''
claster_name = ''
question = ''

for line in df.values.tolist():
    if str(line[1]) != 'nan' and str(line[2]) == 'nan' and group_name:
        group_name = ''
        claster_name = ''
        question = ''



    if str(line[1]) != 'nan' and str(line[2]) == 'nan':
        group_name = line[1]
        structure.setdefault(group_name, {})
    elif str(line[1]) != 'nan' and str(line[2]) != 'nan':
        claster_name = line[1]
        structure[group_name].setdefault(claster_name, {})

    question = line[2]
    if question and str(question) != 'nan':
        structure[group_name][claster_name].setdefault(question, {})
        for question_num, answer_question_num in zip(line[3:13], line[13:23]):
            # здесь '-1' возвращается в question если не указан номер вопроса
            question_num = abs(int(question_num)) if str(question_num) != 'nan' else -1
            answer_question_num = int(answer_question_num)  if str(answer_question_num) != 'nan' else -1
            buffer = {
                question_num: answer_question_num
            }

        structure[group_name][claster_name][question].update(buffer)

with open('key.json', 'w', encoding='utf-8') as f_json:
    json.dump(structure, f_json, ensure_ascii=False, indent=3)
#
