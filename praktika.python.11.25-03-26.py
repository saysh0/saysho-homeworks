#task1 Аннотации для функций
# Для каждой из функций, выбранных для решения, добавьте аннотации типов
# принимаемых и возвращаемых значений функции.
# 1.1. Фильтрация четных с функцией
# Напишите функцию-предикат, которая проверяет четный ли переданный элемент.
# Также напишите функцию, которая принимает функцию-предикат и список чисел.
# Она должна возвращать новый список, содержащий только элементы, для которых
# предикат возвращает True.
# Данные:
# nums = [1, 2, 3, 4, 5, 6]
# Пример вывода:
# [2, 4, 6]

# nums = [1, 2, 3, 4, 5, 6]
# def even_digit(digit: int) -> bool:
#     """
#     Checks whether the digit is even.
#
#     :param digit: Input digit.
#     :return: Returns boolean value.
#     """
#     return not digit % 2
#
# from typing import Callable
# def func_interpretor(func: Callable[[int], bool], your_list: list[int]):
#     """
#     Receives function for value checking.
#
#     :param func: Your func for interpretation.
#     :param your_list: Your list.
#     :return:
#     """
#     return [element for element in your_list if func(element)]
# print(func_interpretor(even_digit, nums))

# task1.2. Фильтрация четных с filter
# Выполните те же условия, что в задаче "Фильтрация списка с функцией", но решите с
# помощью filter и lambda.
# Данные:
# nums = [1, 2, 3, 4, 5, 6]
# Пример вывода:
# [2, 4, 6]

# nums = [1, 2, 3, 4, 5, 6]
# print(list(filter(lambda x: not x % 2, nums)))

#task2.1. Фильтрация списка строк.
# Отфильтруйте в новый список только слова, длина которых больше трех символов.
# Реализуйте в виде функции.
# Данные:
# words = ["hi", "Hello", "a", "python", "Ok"]

# words = ["hi", "Hello", "a", "python", "Ok"]
# def new_list_with_long_words(lst: list[str]) -> list[str]:
#     """
#     Puts words into a list only in word is longer or equal to 3.
#
#     :param lst: List of words.
#     :return: Returns list of long words.
#     """
#     return [word for word in lst if len(word) > 3]
# print(new_list_with_long_words(words))

#task2.2. Фильтрация списка строк по длине.
# Доработайте функцию так, чтобы можно было передавать значение минимальной
# длины слов, которые нужно оставить.
# words = ["hi", "Hello", "a", "python", "Ok"]
# min_len = 2
# Пример вывода:
# ['hi', 'Hello', 'python', 'Ok']

# words = ["hi", "Hello", "a", "python", "Ok"]
# def new_list_with_long_words(lst: list[str], user_word_len: int) -> list[str]:
#     """
#     Puts words into a list only in word is longer or equal to 3.
#
#     :param user_word_len:
#     :param lst: List of words.
#     :return: Returns list of long words.
#     """
#     return [word for word in lst if len(word) >= user_word_len]
# print(new_list_with_long_words(words, 2))
# print(new_list_with_long_words(words, 3))

#task2.3. Фильтрация списка строк по критерию.
# Доработайте функцию так, чтобы можно было передавать критерии отбора слов,
# которые нужно оставить. Например:
# ● слова, начинаются с заглавной буквы
# ● слова из одного символа
# ● слова начинаются и заканчиваются одной буквой, независимо от регистра
# words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
# Пример вывода:
# ['Hello', 'Ok', 'Radar']
# ['a']
# ['a', 'Radar']

# words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
#
# def upper_casee(word: str) -> bool:
#     if word[0].isupper():
#         return True
#
# def length_1(word: str) -> bool:
#     if len(word) == 1:
#         return True
#
# def first_last_letter(word: str) -> bool:
#     if word[0].lower() == word[-1]:
#         return True
#
# from typing import Callable, Any
# def new_list_with_long_words(lst: list[str], func: Callable[[Any], Any]) -> list[str]:
#     """
#     Puts words into a list only if word is longer or equal to 3.
#
#     :param lst: List of words.
#     :return: Returns list of long words.
#     """
#     return [word for word in lst if func(word)]
#
# print(new_list_with_long_words(words, upper_casee))
# print(new_list_with_long_words(words, length_1))
# print(new_list_with_long_words(words, first_last_letter))

#task3 Агрегирование списка.
# Вычислите произведение всех элементов списка с помощью функции высшего
# порядка.
# Данные:
# numbers = [1, 2, 3, 4, 5]
# Пример вывода:
# 120

# numbers = [1, 2, 3, 4, 5]
# def sum_element_list(lst: list) -> int:
#     res = 1
#     for item in lst:
#         res *= item
#     return res
# print(sum_element_list(numbers))
#
# from functools import reduce
# print(reduce(lambda x, y: x * y, numbers))

#task4 Сортировка списка по длине.
# Отсортируйте список слов по длине, используя параметр.
# Данные:
# words = ["apple", "banana", "kiwi", "grape"]
# print(sort_by_length(words))
# Пример вывода:
# ['kiwi', 'grape', 'apple', 'banana']

# words = ["apple", "banana", "kiwi", "grape"]
# def sort_by_length(lst: list[str]) -> list[str]:
#     return sorted(lst, key=len)
# print(sort_by_length(words))

#task5 Очередь с ограничением времени.
# Реализуйте функцию, которая принимает очередь задач с указанием времени их
# выполнения и лимит.
# Если суммарное время превышает заданный лимит, программа должна удалять из
# очереди задачи с минимальным временем выполнения, пока лимит не будет
# соблюдён или не останется выполнимых за остаток времени задач.
# Данные:
# tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}
# time_limit = 10
# Пример вывода:
# Задачи с лимитом по времени:
# {'task3': 7, 'task2': 3}

tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}
def task_queue(kwargs: dict[str, int], time_limit: int):
    tasks_to_delete = []
    for task, time in kwargs.items():
        if time_limit >= time:
            time_limit -= time
        else:
            tasks_to_delete.append(task)

    for task in tasks_to_delete:
        del kwargs[task]
    return kwargs
print(task_queue(tasks, 10))

def task_queue(kwargs: dict, time_limit: int):
    # Создаем отфильтрованный словарь
    filtered = {k: v for k, v in kwargs.items() if time_limit >= v and (time_limit := time_limit - v) is not None}
    # Очищаем оригинал и записываем в него новые данные
    return filtered
print(task_queue(tasks, 10))

def task_queue(kwargs: dict):
    time_limit = 10
    end_dict = {}
    kwargs = sorted(kwargs.items(), key=lambda item: -item[1])
    while time_limit != 0 and kwargs:
        task, time = kwargs.pop(0)
        if time_limit - time < 0:
            continue
        time_limit -= time
        end_dict[task] = time
    return end_dict
print(task_queue(tasks))