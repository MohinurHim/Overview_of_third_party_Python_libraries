# "Обзор сторонних библиотек Python"
from cProfile import label

import pandas as pd
import pylab as p
import requests
import pandas
import matplotlib.pyplot as plt
#requests - библиотека, которая позволяет взаимодействовать с веб - ресурсами и глобальной сетью.
# Предоставляет обширный пул функций для работы со всеми видами HTTP-запросов.
# 1
req = 'https://google.com'
response = requests.get(req) # для чтения интернет ресурса
response.raise_for_status() # для проверки сервиса
print(response.text) # для получения текст ответа
# 2
data_response = requests.post('https://httpbin.org/post', data={'foo': 'bar'}) # запрашивает веб-сервир для приема данных, data- аргумент, который принимает на вход словарь.
print(data_response.text)
# 3
response1 = requests.get('https://httpbin.org/head')
print(response1.text)
print(response1.headers) # возвращает пустое тело ответа

#pandas - библиотека, которая предназначена для обработки и анализа структурированных данных.
# Включает в себя преобразование данных. Pandas Data Frame - структуры которые состоят из данных, организованных в двух измерениях - строках и столбцах, соответствующих им меток.
# 1
data = {'name': ['Masha', 'Anna', 'Jana'], 'age': [22, 30, 25]} # метки столбцов с данными
row_labels = [1, 2, 3] # метки строк
df = pd.DataFrame(data=data, index=row_labels) # ссылка на объект
print(df.head(n=2)) # чтобы увидеть первые 2 элемента
# 2
print(df.tail(n=2)) # для показа последних
# 3
print(df.loc[1]) # доступ ко всей строке

# matplotlib - библиотека для визуализации данных в Python. Для создания графиков, диаграмм и тд.
# 1
x = ['January', 'February', 'March', 'April', 'May']
y = [2, 3, 5, 4, 1]
plt.plot(x, y) # функция которая строит график в соответствии со значениями
plt.show()  # функция которая отвечает за вывод
# 2
plt.bar(x, y, label=label) # функция построения диаграммы, label- задает название величины
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Diagram')
plt.legend() # чтобы включить легенду в диаграмму (область описывающая компоненты)
plt.show()
# 3
vals = [40, 25, 35, 20, 10]
labels = ['January', 'February', 'March', 'April', 'May']
plt.pie(vals, labels=labels)
plt.title('Circle diagram')
plt.show()