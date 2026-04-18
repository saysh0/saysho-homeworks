#task1 План по дням недели
# Напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.
# Данные:
# # Расписание дел на неделю
# weekly_schedule = {
#
#     "Monday": ["Gym", "Work", "Read book"],
#
#     "Tuesday": ["Meeting", "Work", "Study Python"],
#
#     "Wednesday": ["Shopping", "Work", "Watch movie"],
#
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#
#     "Friday": ["Work", "Dinner with friends"],
#
#     "Saturday": ["Hiking", "Rest"],
#
#     "Sunday": ["Family time", "Rest"]
#
# }
# Пример ввода:
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана:
# Tuesday: Meeting, Work, Study Python
# Нажмите 'Enter' для получения плана:
# Sunday: Family time, Rest
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана: q
#
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Rest"],

    "Sunday": ["Family time", "Rest"]
}

import itertools
iterable = itertools.cycle(weekly_schedule.items())
while True:
    user_info = input('Нажмите "Enter" для получения плана (или "q" для выхода): ')
    if user_info.lower() == 'q':
        break
    elif user_info.lower() != '':
        continue
    day, tasks = next(iterable)
    result = ', '.join(tasks)
    print(f'{day}: {result}')

#task2 Объединение списков продуктов
# Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, содержащий все продукты в нижнем регистре.
# Выведите содержимое генератора.
# Данные:
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
# Пример вывода:
# apple
# banana
# orange
# carrot
# tomato
# cucumber
# milk
# cheese
# yogurt

import itertools
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]
def all_items_in_list(*lists):
    x = itertools.chain(*lists)
    return (item.lower() for item in x)

for i in all_items_in_list(fruits, vegetables, dairy):
    print(i)

#task3 Комбинации одежды
# Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
# в формате "Clothe - Color - Size".
# Данные:
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
# Пример вывода:
# T-shirt - Red - S
# T-shirt - Red - M
# T-shirt - Red - L
# T-shirt - Blue - S
# ...
# Jacket - Black - L

import itertools
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]
def cloth_combinations(*iterables):
    return (' - '.join(item) for item in itertools.product(*iterables))

print(cloth_combinations(clothes, colors, sizes))

for item in cloth_combinations(clothes, colors, sizes):
    print(item)