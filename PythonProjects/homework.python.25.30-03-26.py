# task1 Деление без ошибок.
# Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.

# num1 = input('Введите делимое: ')
# num2 = input('Введите делитель: ')
# def divide_num(n1, n2) -> float:
#     '''
#     Функция принимает 2 числа, где (1.Делимое, 2.Делитель) и выводит их результат деления.
#
#     :param n1: Принимает число(int), а также число с плавающей запятой(float) которое является делимым.
#     :param n2: Принимает число(int), а также число с плавающей запятой(float) которое является делителем.
#     :return: Результат деления делителя(param(n1)) на делимое(param(n2)).
#     '''
#     n1 = float(n1)
#     n2 = float(n2)
#     if float(n1) == 0 or float(n2) == 0:
#         raise ZeroDivisionError
#     return n1 / n2
#
# try:
#     print(divide_num(num1, num2))
# except ZeroDivisionError:
#     print('Вы ввели ноль, деление на ноль не возможно.')
# except ValueError:
#     print('Вы ввели знак не являющийся числом.')

# task2 Логирование ошибок.
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.homework.python.25.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

import logging

logging.basicConfig(level=logging.DEBUG, filename='errors.homework.python.25.log',
                    format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s", filemode='w',
                    encoding='utf-8')


def divide_num(n1, n2) -> float:
    '''
    Функция принимает 2 числа, где (1.Делимое, 2.Делитель) и выводит их результат деления.

    :param n1: Принимает число(int), а также число с плавающей запятой(float) которое является делимым.
    :param n2: Принимает число(int), а также число с плавающей запятой(float) которое является делителем.
    :return: Результат деления делителя(param(n1)) на делимое(param(n2)).
    '''
    n1 = float(n1)
    n2 = float(n2)
    if float(n1) == 0 or float(n2) == 0:
        raise ZeroDivisionError('Вы ввели ноль, деление на ноль не возможно.')
    logging.info(f"Успешное деление: {n1} / {n2} = {n1 / n2}")
    return n1 / n2

numer1 = input('Введите делимое: ')
numer2 = input('Введите делитель: ')

try:
    print(divide_num(numer1, numer2))
except ZeroDivisionError as e:
    logging.error(f"Ошибка деления на ноль: {e}")
    print('Вы ввели ноль, деление на ноль не возможно.')
except ValueError:
    logging.warning(f"Пользователь ввел данные не являющиеся числом(int) или число с плавающей точкой(float)")
    print('Вы ввели знак не являющийся числом.')