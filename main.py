import json
from copy import deepcopy

import pandas as pd
from pprint import pprint


df_key = pd.read_excel('ключ оценка 360.xlsx', sheet_name='данные')

list_of_questions = [line[0] for num, line in enumerate(df_key.values.tolist()) if str(line[0]) != 'nan']

df_key = pd.read_excel('ключ оценка 360.xlsx', sheet_name='Ключ')
df_answers = pd.read_excel('ключ оценка 360.xlsx', sheet_name='перевод обратных')

# print(*df.values.tolist(), sep='\n')
structure = {}
group_name = ''
claster_name = ''
question = ''

for line_key, line_answer in zip(df_key.values.tolist(), df_answers.values.tolist()):
    if str(line_key[1]) != 'nan' and str(line_key[2]) == 'nan' and group_name:
        group_name = ''
        claster_name = ''
        question = ''



    if str(line_key[1]) != 'nan' and str(line_key[2]) == 'nan':
        group_name = line_key[1]
        structure.setdefault(group_name, {})
    elif str(line_key[1]) != 'nan' and str(line_key[2]) != 'nan':
        claster_name = line_key[1]
        structure[group_name].setdefault(claster_name, {})

    question = line_key[2]
    if question and str(question) != 'nan':
        structure[group_name][claster_name].setdefault(question, {})
        a = zip(line_key[3:13], line_answer[14:23])
        for question_num, answer_question_num in zip(line_key[3:13], line_answer[14:24]):

            # здесь '-1' возвращается в question если не указан номер вопроса
            if str(question_num) == 'nan' and str(answer_question_num) == 'nan':
                continue
            question_num = abs(int(question_num))
            answer_question_num = int(answer_question_num)
            buffer = {
                question_num: answer_question_num
            }
            print(buffer, type(str(buffer[question_num])), type(str(question_num)))


            structure[group_name][claster_name][question].update(deepcopy(buffer))

with open('key.json', 'w', encoding='utf-8') as f_json:
    json.dump(structure, f_json, ensure_ascii=False, indent=3)
#
