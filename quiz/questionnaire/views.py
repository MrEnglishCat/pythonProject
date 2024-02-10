import re
import random
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseBadRequest
import pandas as pd
from .forms import QuestionForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def questionnaire(request):
    file = 'ключ оценка 360.xlsx'
    result = []
    # Загружаем spreadsheet в объект pandas
    xl = pd.ExcelFile(file)

    # Печатаем название листов в данном файле
    print(xl.sheet_names)
    print()
    # Загрузить лист в DataFrame по его имени: df1
    df1= xl.parse(xl.sheet_names[0])
    indexes = df1.index.tolist()  # список индексов
    indexes = df1.index.tolist()  # список индексов
    df1.columns.tolist()  # Получение списка названий столбцов
    # print('===', df1.iloc[0:10])
    print('===', df1)
    for idx, row in df1.iterrows():
        if idx < 4:
            continue
        result.append(re.split(r'(?<=\d.) ', row.values[0]))
    random.shuffle(result)

    original_data_result = {}

    for k, v in result:
        form = QuestionForm(v)
        # form.question = v
        # original_data_result[form] = int(k.strip('.'))
        original_data_result[int(k.strip('.'))] = form

    res_dict = {}

    return  render(request, 'questionnaire_web_page/questionnaire_web_page.html', {'data':enumerate(original_data_result.values(), 1), 'form':form})