#task1 Список файлов и папок.
# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
# Отдельно список папок
# Отдельно список файлов
# Пример запуска
# python script.py /home/user/documents
# Пример вывода
# Содержимое директории '/home/user/documents':
# Папки:
# - folder1
# - folder2
# Файлы:
# - file1.txt
# - file2.txt
# - notes.docx

import os
import sys
# path_to_dir = sys.argv[1]
# print(f'Содержимое директории: {path_to_dir}')
# print('Папки:')
# for root, dirs, files in os.walk(path_to_dir):
#     for dir in dirs:
#         print(f"-{dir}\n")
# print('Файлы:')
# for root, dirs, files in os.walk(path_to_dir):
#     for file in files:
#         print(f"-{file}\n")

#task2 Поиск и удаление файлов с указанным расширением.
# Напишите программу, которая:
# Принимает путь к директории и расширение файлов через аргумент командной строки.
# Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
# Спрашивает у пользователя, хочет ли он удалить найденные файлы.
# Если пользователь подтверждает, удаляет их.
# Пример запуска:
# python script.py /home/user/PycharmProjects/project1 .log
# Пример вывода
# Найдены файлы с расширением '.log':
# - logs/error.log
# - logs/system.log
# - logs/backup/old.log
# - logs/backup/debug.log
# Вы хотите удалить эти файлы? (y/n): y
# Удаление завершено.

path_to_dir = sys.argv[1]
for dirpath, dirnames, filenames in os.walk(path_to_dir):
    for filename in filenames:
        if filename.endswith(".log"):
            print(f'Найден файл с расширением ".log":\n -{os.path.join(dirpath, filename)}')
            flag = True
            while flag:
                user_answer = input('Вы хотите ли удалить этот файл? (y/n): ').lower()
                try:
                    if user_answer not in ('y', 'n'):
                        raise ValueError('Вы ввели неподходящий символ по регистру или значению, надо ввести y(да) или n(нет).')
                except ValueError as b:
                    print(f'Упс! Что то пошло не так, ваш ответ вызвал ошибку: {b}')
                else:
                    if user_answer == 'y':
                        os.remove(os.path.join(dirpath, filename))
                        print('Удаление завершено.')
                        flag = False
                    else:
                        pass
                        flag = False