# encoging utf-8-sig

import os
import time
from pprint import pprint

print('Игра Крестики-Нолики началась!')
EMPTY = 8
maps = {
    '1': {
        'a': '_',
        'b': '_',
        'c': '_'
    },
    '2': {
        'a': '_',
        'b': '_',
        'c': '_'
    },
    '3': {
        'a': '_',
        'b': '_',
        'c': '_'
    }
}

allowed_rows = ('1', '2', '3')
allowed_column = ('a', 'b', 'c')
allowed_values = ('X', 'O')


def print_game_field():
    print('\t', '\t\t'.join(allowed_column), end='\n\n')
    print(f"1\t {maps['1']['a']}\t\t{maps['1']['b']}\t\t{maps['1']['c']}\n")
    print(f"2\t {maps['2']['a']}\t\t{maps['2']['b']}\t\t{maps['2']['c']}\n")
    print(f"3\t {maps['3']['a']}\t\t{maps['3']['b']}\t\t{maps['3']['c']}\n")


def input_value(input_value):
    global EMPTY
    is_Errors = False
    for data in maps.values():
        for d in data.values():
            if d =="_":
                EMPTY -= 1

    if len(input_value) > 3:
        print('Формат ввода значения: 1aX.\n\t1 - строка\n\ta - столбец\n\tX or x - крестик или нолик\n\t Вы пропускаете ход!\n\n')
        return
    row = input_value[0]
    if row not in allowed_rows:
        is_Errors = True
        print(f'Введено неверное значение строки! Вы ввели: {row}.\n\t Доступные значения: {", ".join(allowed_rows)}\n\t Вы пропускаете ход!')
    column = input_value[1]
    if column not in allowed_column:
        is_Errors = True
        print(
            f'Введено неверное значение столбца! Вы ввели: {column}.\n\t Доступные значения: {", ".join(allowed_column)}\n\t Вы пропускаете ход!')
    value = input_value[2].upper()
    if value not in allowed_values:
        is_Errors = True
        print(
            f'Введено неверное значение столбца! Вы ввели: {value}.\n\t Доступные значения(строчные и прописные): {", ".join(allowed_values)}\n\t Вы пропускаете ход!')
    if is_Errors:
        return

    if maps[row][column] != '_':
        print(f'Указанная ячейка уже заполнена занчением {maps[row][column]}!\n\t Вы пропускаете ход!')
        return
    if current_palayer == 'X' and value == "X":
        maps[row][column] = value
        is_win()
    else:
        print(f"Сейчас ход '{current_palayer}', а вы ввели {value}! Вы пропускаете ход!")
        return

def is_win():
    winner = 'Игра продолжается!\n'
    is_winner = False
    # 1 заполнена любая из строк символом Х или О
    if maps['1']['a'] == maps['1']['b'] == maps['1']['c'] != '_':
        is_winner = True
        winner = maps['1']['a']
    elif maps['2']['a'] == maps['2']['b'] == maps['2']['c'] != '_':
        is_winner = True
        winner = maps['2']['a']
    elif maps['3']['a'] == maps['3']['b'] == maps['3']['c'] != '_':
        is_winner = True
        winner = maps['3']['a']


    # 2 заполнен любой столбец символом Х или О
    elif maps['1']['a'] == maps['2']['a'] == maps['3']['a'] != '_':
        is_winner = True
        winner = maps['1']['a']
    elif maps['1']['b'] == maps['2']['b'] == maps['3']['b'] != '_':
        is_winner = True
        winner = maps['1']['b']
    elif maps['1']['c'] == maps['2']['c'] == maps['3']['c'] != '_':
        is_winner = True
        winner = maps['1']['c']

    # 3 заполнена либо главная диагональ, либо побочная
    elif maps['1']['a'] == maps['2']['b'] == maps['3']['c'] != '_':
        is_winner = True
        winner = maps['1']['a']
    elif maps['1']['c'] == maps['2']['b'] == maps['3']['a'] != '_':
        is_winner = True
        winner = maps['1']['b']

    elif not EMPTY:
        is_winner = True
        print('Ничья')
        winner = 'Ничья'

    if is_winner:
        print(f'Выйграли "{winner}"')
        print('Очистка игрового поля...')
        time.sleep(2)
        reset_values()
        print('Игровое поле очищено!')
        if (a := input('Желаете сыграть еще раз? (y/[any else])')) != 'y':
            global start_game
            start_game = False


def reset_values():
    maps['1']['a'] = '_'
    maps['1']['b'] = '_'
    maps['1']['c'] = '_'
    maps['2']['a'] = '_'
    maps['2']['b'] = '_'
    maps['2']['c'] = '_'
    maps['3']['a'] = '_'
    maps['3']['b'] = '_'
    maps['3']['c'] = '_'


def run_game():

    input_value(input(f'Ваш ход, {current_palayer}:'))
    print_game_field()


start_game = True
current_palayer = "X"
print_game_field()
while start_game:
    run_game()
    if current_palayer == "X":
        current_palayer = 'O'
    else:
        current_palayer = 'X'

# import pandas as pd`

#
# file = 'ключ оценка 360.xlsx'
#
#
# # Загружаем spreadsheet в объект pandas
# xl = pd.ExcelFile(file)
#
# # Печатаем название листов в данном файле
# print(xl.sheet_names)
# print()
# # Загрузить лист в DataFrame по его имени: df1
# df1:xl = xl.parse(xl.sheet_names[1])
# indexes = df1.index.tolist() # список индексов
# indexes = df1.index.tolist() # список индексов
# df1.columns.tolist()# Получение списка названий столбцов
# # print('===', df1.iloc[0:10])
# print('===', df1)
#
# for idx, row in df1.iterrows():
#     print(idx, row.iloc[1])
