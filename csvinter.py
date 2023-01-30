#!/bin/python3
import csv
import re
import sys

table_csv = sys.argv[1] # считываем название файла в терминале (просто имя файла - если он в одной папке со скриптом, или путь до файла)

with open (str(table_csv)) as file:
    reader = csv.reader(file) # открываем файл на чтение
    rw = {}
    for row in reader: 
        rw[row[0]] = row[1: len(row)] # заполняем словарь, где ключи - названия строк (по ключу '' будут храниться названия столбцов)

try:
    for val in rw.values():
        for dat in val:
            if '=' in dat:
                if re.search(r'[a-zA-Z]+', dat): # проверяем, находится ли в ячейке выражение с ссылками
                    columns = re.findall(r'[a-zA-Z]+', dat)  # Записываем имена столбцов таблицы (они дольжны состоять из латинских букв)
                    rows = re.findall(r'\d+', dat) # номера строк - целые положителные числа
                    #расчитываем значение в ячейке (значение в строке берется по индексу названия столбца)
                    if '+' in dat:
                        metadat = str(int(rw[rows[0]][rw[''].index(columns[0])]) + int(rw[rows[1]][rw[''].index(columns[1])])) 
                    elif '-' in dat:
                        metadat = str(int(rw[rows[0]][rw[''].index(columns[0])]) - int(rw[rows[1]][rw[''].index(columns[1])]))
                    elif '/' in dat:
                        metadat = str(int(rw[rows[0]][rw[''].index(columns[0])]) // int(rw[rows[1]][rw[''].index(columns[1])]))
                    elif '*' in dat:
                        metadat = str(int(rw[rows[0]][rw[''].index(columns[0])]) * int(rw[rows[1]][rw[''].index(columns[1])]))
                        
                    val[val.index(dat)] = dat.replace(dat, metadat) # заменяем выражение на результат

                else: # если обозначено как выражение и нет ссылок - считаем выражение
                    numbs = re.findall(r'\d+', dat)
                    if '+' in dat:
                        metadat = str(int(numbs[0]) + int(numbs[1]))
                    elif '-' in dat:
                        metadat = str(int(numbs[0]) - int(numbs[1]))
                    elif '/' in dat:
                        metadat = str(int(numbs[0]) // int(numbs[1]))
                    elif '*' in dat:
                        metadat = str(int(numbs[0]) * int(numbs[1]))
                        
                    val[val.index(dat)] = dat.replace(dat, metadat) # заменяем выражение на результат

    for k, v in rw.items():
        print(k, *v)        #построчно выводим таблицу

except TypeError:
    print('AN ERROR OCCURED! TRY TO CHECK DATA IN YOUR CSV FILE!')       
except FileNotFoundError:
    print('AN ERROR OCCURED! TRY TO CHECK YOUR CSV FILE NAME OR FILEPATH')
except LookupError:
    print('AN ERROR OCCURED! TRY TO CHECK YOUR LINKS IN CELLS')
except ArithmeticError:
    print('AN ERROR OCCURED! TRY TO CHECK YOUR MATH EXPRESSIONS IN CELLS')
except ValueError:
    print('AN ERROR OCCURED! TRY TO CHECK VALUES FOR YOUR MATH EXPRESSIONS')

