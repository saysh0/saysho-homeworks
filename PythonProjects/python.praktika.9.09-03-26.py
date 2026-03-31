# task1 Числа кратные 3 или 5.
# Напишите программу, которая создает множество из чисел, фильтруя элементы, не кратные 3 или 5.
# Данные:
# numbers = [16, 18, 1, 6, 3, 2, 6, 2, 14, 3, 20, 15, 19, 4, 18, 15, 15, 4, 20, 18]
# Пример вывода:
# {3, 6, 15, 18, 20}

# numbers = [16, 18, 1, 6, 3, 2, 6, 2, 14, 3, 20, 15, 19, 4, 18, 15, 15, 4, 20, 18]
# print({num for num in numbers if num % 3 == 0 or num % 5 == 0})

#task2 Проверка уникальности ключей.
# Напишите программу, которая проверяет, содержатся ли в двух заданных словарях одинаковые ключи.
# Вывести одинаковые ключи или "-", если таковых нет.
# Данные:
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 5, "d": 7, "a": 8}
# Пример вывода:
# Общие ключи: ['a', 'b']

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 5, "d": 7, "a": 8}
# same_keys = dict1.keys() & dict2.keys()
# print(list(same_keys) if same_keys else '-')

#task3 Строки с длиной.
# Напишите программу, которая преобразует список строк в словарь, где ключи — сами строки, а значения —
# их длины.
# Данные:
# words = ["apple", "banana", "cherry", "date"]
# Пример вывода:
# {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

# words = ["apple", "banana", "cherry", "date"]
# print({key: len(key) for key in words})

#task4 Проверка подмножества.
# Напишите программу, которая проверяет, является ли один словарь подмножеством другого (т.е. все его пары
# "ключ-значение" содержатся в другом словаре).
# Данные:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 2, "c": 3}
# Пример вывода:
# Первый словарь является подмножеством второго.

# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 2, "c": 3}
# issubset1 = dict1.items() <= dict2.items()
# print('Первый словарь является подмножеством второго.' if issubset1 else 'Первый словарь не является подмножеством второго.')

#task5 Удаление пустых значений.
# Напишите программу, которая удаляет из словаря все пары "ключ-значение", где значение пустое (например,
# None, пустая строка или пустой список).
# Данные:
# data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
# Пример вывода:
# {'b': 2, 'e': [1, 2]}

# data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
# print({key: value for key, value in data.items() if value})

#task6 Потерянные страницы книги.
# Вам дан словарь, где ключи — номера страниц книги, а значения — содержимое страниц. Некоторые
# страницы отсутствуют (значения None). Напишите программу, которая на пропущенных страницах заменит
# значение на "Страница потеряна".
# Данные:
# book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}

# book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}
# print('Измененный вариант:',{key: value if value else 'Страница потеряна' for key, value in book.items()})

#task7 База оценок студентов.
# У вас есть словарь с именами студентов и списками их оценок. Напишите программу, которая вычисляет
# средний балл для каждого студента. Далее нужно сохранить средний балл в значениях для каждого студента,
# как показано на примере.
# Данные:
# grades = {
#  "anna": [5, 4, 3, 5],
#  "bennet": [3, 2, 4],
#  "john": [5, 5, 5]
# }
# Пример вывода:
# {'anna': {'оценки': [5, 4, 3, 5], 'средний балл': 4.25}, 'bennet': {'оценки': [3, 2, 4], 'средний балл': 3.0},
# 'john': {'оценки': [5, 5, 5], 'средний балл': 5.0}}

# grades = {
#  "anna": [5, 4, 3, 5],
#  "bennet": [3, 2, 4],
#  "john": [5, 5, 5]
# }
# new_dict = {}
# for key, value in grades.items():
#     new_dict[key] = {'оценки': value, 'средний бал': sum(value)/len(value)}
# print(new_dict)

#task8 Рецепты по ингредиентам.
# Создайте словарь, в котором для каждого набора ингредиентов будут храниться все названия рецептов.
# Учитывайте что ингредиенты могут быть перечислены в произвольном порядке и некоторые рецепты могут
# иметь одинаковые ингредиенты.
# Выведите возможные рецепты для каждого набора продуктов.
# В конце пользователь вводит список имеющихся у него ингредиентов через пробел, и программа должна
# вывести названия всех доступных рецептов. Если рецептов нет, нужно вывести сообщение "Нет рецептов".
# Данные:
# recipes = {
#  ("flour", "egg", "milk"): "Pancakes",
#  ("egg", "milk", "butter"): "Omelette",
#  ("flour", "sugar", "butter"): "Cookies",
#  ("flour", "egg", "butter", "sugar"): "Cake",
#  ("milk", "flour", "egg"): "Waffles",
#  ("butter", "milk", "egg"): "Scrambled Eggs",
#  ("flour", "milk", "sugar", "butter"): "Sweet Bread"
# }
# Пример ввода:
# milk egg butter flour

# recipes = {
#  ("flour", "egg", "milk"): "Pancakes",
#  ("egg", "milk", "butter"): "Omelette",
#  ("flour", "sugar", "butter"): "Cookies",
#  ("flour", "egg", "butter", "sugar"): "Cake",
#  ("milk", "flour", "egg"): "Waffles",
#  ("butter", "milk", "egg"): "Scrambled Eggs",
#  ("flour", "milk", "sugar", "butter"): "Sweet Bread"
# }
# ingridients = set('milk egg butter flour'.lower().split())
# new_dict = []
# for products, name in recipes.items():
#     key = set(products) <= ingridients
#     if key:
#         new_dict.append(name)
# print(new_dict if new_dict else 'Нет рецептов')

# task9 Одинаковые предметы.
# Есть список студентов и наборы предметов, которые они изучают.
# Необходимо сгруппировать студентов по идентичным наборам предметов, используя frozenset как ключ, и
# вывести группы.
# Данные:
# students = {
#  "Alice": ["Math", "Physics"],
#  "Bob": ["Math", "Physics"],
#  "Charlie": ["Chemistry", "Biology"],
#  "David": ["Math", "Physics"],
#  "Eve": ["Chemistry", "Biology"]
# }
# Пример вывода:
# Группа с предметами: Physics, Math: ['Alice', 'Bob', 'David']
# Группа с предметами: Biology, Chemistry: ['Charlie', 'Eve']

# students = {
#  "Alice": ["Math", "Physics"],
#  "Bob": ["Math", "Physics"],
#  "Charlie": ["Chemistry", "Biology"],
#  "David": ["Math", "Physics"],
#  "Eve": ["Chemistry", "Biology"]
# }
# group_lessons = {}
# for student, subjects in students.items():
#     subjects_frozen = frozenset(subjects)
#     group_lessons.setdefault(subjects_frozen, []).append(student)
# for lessons, students in group_lessons.items():
#     print(", ".join(lessons),':',students)