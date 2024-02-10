print(*(i for i in range(1,10) if i % 2))

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
