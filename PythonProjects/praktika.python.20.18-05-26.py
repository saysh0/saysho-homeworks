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

#task1 Список сотрудников по убыванию зарплаты.
# Добавьте к программе сортировку сотрудников выбранного департамента по убыванию зарплаты. Выведите имя,
# фамилию, должность и зарплату каждого сотрудника, начиная с самого высокооплачиваемого. Также добавьте
# нумерацию (не id).
# Пример вывода:
# Enter department: Marketing
# 1. Michael Hartstein — Marketing Manager — 13000.00
# 2. Pat Fay — Marketing Representative — 6000.00

#task2 Выбор департамента по номеру.
# Модифицируйте предыдущую программу так, чтобы пользователь выбирал департамент по номеру из списка, а
# не вручную вводил его название. После выбора выведите название департамента и продолжите выполнение.
# Пример вывода:
# Enter department number: 2
# You choose: Marketing
# 1. Michael Hartstein — Marketing Manager — 13000.00
# 2. Pat Fay — Marketing Representative — 6000.00

#task3 Пустой департамент.
# Добавьте в программу проверку: если в выбранном департаменте нет сотрудников, вместо списка
# сотрудников выведите сообщение:
# No employees found in this department.
# Пример вывода:
# Enter department number: 27
# You selected: Payroll
# No employees found in Payroll department.

#task4 Фильтрация сотрудников по зарплате.
# Если в выбранном департаменте есть сотрудники — добавьте возможность отфильтровать
# их по зарплате.
# Спросите пользователя:
# Would you like to filter employees by salary? (y/n)
# Если ответ — y, попросите ввести знак сравнения и значение:
# Enter condition (>, <, =, >=, <=): >
# Enter salary: 13000
# Затем выведите только тех сотрудников, которые соответствуют критерию. Если ответ n, просто выведите всех сотрудников.
# Пример вывода:
# Enter department number: 8
# You selected: Sales
# Would you like to filter employees by salary? (y/n) y
# Enter condition (>, <, =, >=, <=): >
# Enter salary: 13000
# 1. John Russell — Sales Manager — 14000.00
# 2. Karen Partners — Sales Manager — 13500.00

#task5 Повторный ввод при ошибке
# Модифицируйте программу так, чтобы при вводе некорректного номера департамента
# пользователю предлагалось ввести его снова. Программа не должна завершаться, пока не
# будет введён корректный номер.
# Пример вывода:
# Enter department number: 999
# Invalid department number. Please try again.
# Enter department number: num1
# Invalid input. Please enter a number.
# Enter department number: 2
# You selected: Marketing

import operator

ops = {
    ">": operator.gt,
    "<": operator.lt,
    "=": operator.eq,
    "==": operator.eq,
    ">=": operator.ge,
    "<=": operator.le,
}

new_dict = {}
cursor.execute("""SELECT department_name FROM departments""")
for num, row in enumerate(cursor.fetchall(), 1):
    new_dict[num] = row[0]
    print(f'{num} {row[0]}')

while True:
    try:
        user_department_num = int(input('Enter department number from list: '))
    except ValueError:
        print('Invalid input. Please enter a number.')
    else:
        if user_department_num not in new_dict.keys():
            print('Invalid department number. Please try again.')
            continue
        else:
            break

usr_department = ''

for key, value in new_dict.items():
    if key == user_department_num:
        usr_department = value

print(f'Your choose: {usr_department}')
cursor.execute("""SELECT e.first_name, e.last_name, jt.job_title, e.salary
                        FROM employees as e
                        JOIN departments as d ON d.department_id = e.department_id
                        JOIN jobs as jt ON jt.job_id = e.job_id
                        WHERE department_name = %s
                        ORDER BY e.salary desc""", (usr_department,))

employees = cursor.fetchall()

if not employees:
    print('No employees found in this department.')

user_sort_param = input('Would you like to filter employees by salary? (y/n): ').lower().strip()

if user_sort_param == 'y':
    user_condition = input('Enter condition (>, <, =, >=, <=): ').strip()
    user_salary = float(input('Enter salary: '))
    for num, row in enumerate(employees, 1):
        name, second_name, job_title, salary = row
        if user_condition in ops and ops[user_condition](salary, user_salary):
            print(f'{num}. {name} {second_name} -- {job_title} -- {salary}')
else:
    for num, row in enumerate(employees, 1):
        name, second_name, job_title, salary = row
        print(f'{num}. {name} {second_name} -- {job_title} -- {salary}')
cursor.close()