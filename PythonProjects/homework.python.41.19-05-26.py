#task1 Список всех стран.
# Используя базу данных world, выведи названия всех стран из таблицы country. Каждое название должно отображаться с новой строки и иметь номер.

#task2 Города выбранной страны.
# Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка.
# Далее выведите все города этой страны и их численность насиления, также с нумерацией.


import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'test'),
}

conn = pymysql.connect(**config)
cursor = conn.cursor()

cursor.execute('select Name from country')
countrys = {}
for num, country in enumerate(cursor.fetchall(), 1):
    countrys[num] = country[0]
    print(f"{num}. {country[0]}")

print(20 * '-') #для себя

user_country = input('Введите название страны или ее номер из списка: ').lower().strip() #germany num = 57

print(20 * '-') #для себя

if user_country.isdigit():
    user_country = int(user_country)
    for num, country in countrys.items():
        if num == user_country:
            user_country = country

cursor.execute('select Code from country where Name =%s', (user_country,))
country_code = cursor.fetchone()[0]
cursor.execute('select Name, Population from city where CountryCode = %s', (country_code,))
for num, city in enumerate(cursor.fetchall(), 1):
    print(f"{num}. {city[0]} - {city[1]}")


