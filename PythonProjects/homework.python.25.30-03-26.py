#task1 Деление без ошибок.
# Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.

# num1 = input('Введите делимое: ')
# num2 = input('Введите делитель: ')
# def divide_num(numer1, numer2):
#     if not numer1.isdigit() or not numer2.isdigit():
#         raise ValueError('Вы ввели знак не являющийся числом.')
#     if int(numer1) == 0 or int(numer2) == 0:
#         raise ZeroDivisionError('Вы ввели ноль, деление на ноль не возможно.')
# try:
#     divide_num(num1, num2)
# except ZeroDivisionError as a:
#     print(f'Ошибка: {a}')
# except ValueError as b:
#     print(f'Ошибка: {b}')
# else:
#     print(int(num1) / int(num2))



# def divide_num():
#     try:
#         num1 = input('Введите делимое: ')
#         num2 = input('Введите делитель: ')
#         if not num1.isdigit() or not num2.isdigit():
#             raise ValueError('Вы ввели знак не являющийся числом.')
#         if int(num1) == 0 or int(num2) == 0:
#             raise ZeroDivisionError('Вы ввели ноль, деление на ноль не возможно.')
#     except ZeroDivisionError as a:
#         print(f'Ошибка: {a}')
#     except ValueError as b:
#         print(f'Ошибка: {b}')
#     else:
#         print(int(num1) / int(num2))
# divide_num()


# def divide_num():
#     try:
#         num1 = input('Введите делимое: ')
#         num2 = input('Введите делитель: ')
#         res = int(num1) / int(num2)
#     except ZeroDivisionError:
#         print('Вы ввели ноль, деление на ноль не возможно.')
#     except ValueError:
#         print('Вы ввели знак не являющийся числом.')
#     except Exception:
#         print('Ты че еблан, ты как код наебнул')
#     else:
#         print(res)
# divide_num()

num1 = input('Введите делимое: ')
num2 = input('Введите делитель: ')
def divide_num(n1, n2):
    try:
        if int(n1) == 0 or int(n2) == 0:
            raise ZeroDivisionError('Вы ввели ноль, деление на ноль не возможно.')
        res = int(n1) / int(n2)
        return res
    except ZeroDivisionError:
        return 'Вы ввели ноль, деление на ноль не возможно.'
    except ValueError:
        return 'Вы ввели знак не являющийся числом.'
print(divide_num(num1, num2))

#task2 Логирование ошибок.
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.homework.python.25.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

import logging
logging.basicConfig(level=logging.DEBUG, filename='errors.homework.python.25.log', format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s", filemode='w', encoding='utf-8')

numer1 = input('Введите делимое: ')
numer2 = input('Введите делитель: ')
def divide_num(n1, n2):
    try:
        if int(n1) == 0 or int(n2) == 0:
            raise ZeroDivisionError('Вы ввели ноль, деление на ноль не возможно.')
        res = int(n1) / int(n2)
        logging.info(f"Успешное деление: {n1} / {n2} = {res}")
        return res
    except ZeroDivisionError as e:
        logging.error(f"Ошибка деления на ноль: {e}")
        return 'Вы ввели ноль, деление на ноль не возможно.'
    except ValueError:
        logging.warning(f"Пользователь ввел не число: {n1} или {n2}")
        return 'Вы ввели знак не являющийся числом.'
print(divide_num(numer1, numer2))