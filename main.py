import json

import pandas
import pandas as pd
from copy import deepcopy

from pprint import pprint


class Quiz:
    pass



def get_question_list(file_name, sheet_name):
    '''

    :param file_name: 'ключ оценка 360.xlsx'
    :param sheet_name: 'данные'
    :return:
    '''
    df_key = pd.read_excel('ключ оценка 360.xlsx', sheet_name='данные')
    list_of_questions = [line[0] for num, line in enumerate(df_key.values.tolist()) if str(line[0]) != 'nan']

    return list_of_questions

def get_question_groups(file_name:str, sheets:list):
    '''
        Получает данные из файда xlsx и формирует dict

    {
        claster_name: {
            group_name: {
                question_group: {
                    question_num : answer_num
                }
            }
        },
        {
        ....
    }
    :param file_name: 'ключ оценка 360.xlsx'
    :param sheets: ['Ключ', 'перевод обратных']
    :return:
    '''

    df_key = pd.read_excel('ключ оценка 360.xlsx', sheet_name='Ключ')
    df_answers = pd.read_excel('ключ оценка 360.xlsx', sheet_name='перевод обратных')

    structure = {}
    group_name = ''
    claster_name = ''
    question_group = ''

    for line_key, line_answer in zip(df_key.values.tolist(), df_answers.values.tolist()):
        if str(line_key[1]) != 'nan' and str(line_key[2]) == 'nan' and group_name:
            group_name = ''
            claster_name = ''
            question_group = ''



        if str(line_key[1]) != 'nan' and str(line_key[2]) == 'nan':
            group_name = line_key[1]
            structure.setdefault(group_name, {})
        elif str(line_key[1]) != 'nan' and str(line_key[2]) != 'nan':
            claster_name = line_key[1]
            structure[group_name].setdefault(claster_name, {})

        question_group = line_key[2]
        if question_group and str(question_group) != 'nan':
            structure[group_name][claster_name].setdefault(question_group, {})
            a = zip(line_key[3:13], line_answer[14:23])
            buffer = {}
            for question_num, answer_question_num in zip(line_key[3:13], line_answer[14:23]):

                # здесь '-1' возвращается в question если не указан номер вопроса
                if str(question_num) == 'nan' and str(answer_question_num) == 'nan':
                    continue
                question_num = abs(int(question_num))
                answer_question_num = int(answer_question_num)
                buffer.update(
                    {
                        question_num: answer_question_num
                    }
                )

            list_of_answer = buffer.values()
            average_answer = sum(list_of_answer)/len(list_of_answer)
            buffer.update(
                {
                    'AVG':round(average_answer, 4)
                }
            )
            structure[group_name][claster_name][question_group].update(buffer)
    return structure, df_key, df_answers

def write_to_json(data:dict, file_name):
    '''

    :param data: structure : dict
    :param file_name: 'key.json'
    :return: None
    '''
    with open(file_name, 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, ensure_ascii=False, indent=3)


def write_dataframe_to_excel(df_key, df_answer, structure, file_name, sheet_name):
    '''

    :param df_key: pandas.DataFrame()
    :param file_name: 'template.xlsx'
    :param sheet_name: 'Ключ'
    :return:
    '''
    # line_answer[14:23]
    d = df_key.to_numpy()
    for line_id in range(len(df_key)):
        df_key.values[line_id][14:23] = df_answer[line_id][14:23]

    df_key.to_excel(file_name, 'Ключ', index=False, header=False, merge_cells=True)

struncture, df_key, df_answer = get_question_groups('ключ оценка 360.xlsx', ['Ключ', 'перевод обратных'])

write_dataframe_to_excel(df_key, df_answer, struncture, 'template.xlsx', 'Ключ')