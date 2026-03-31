#task1 Число в конце.
# Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка, в которых цифры находятся только в конце.
# Данные:
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# Пример вывода:
# Строки с цифрами только в конце: ['apple23', 'grape3']

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_list = []
for string in strings:
    i = 0
    while i < len(string) and not string[i].isdigit():
        i += 1
    if i < len(string) and string[i:].isdigit():
        new_list.append(string)
print(f'Строки с цифрами в конце: {new_list}')

#task2 Удаление кратных.
# Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
# Данные:
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# Пример вывода:
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
new_list = []
for number in numbers:
    if number % 3 != 0:
        new_list.append(number)
print(f'Список без кратных значений: {new_list}')

#task3 Порядок четных.
# Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,
# чётные числа отсортированы между собой обратном порядке.
# Данные:
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# Пример вывода:
# Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
new_list = []
oven_numbers = []
for num in numbers:
    if num % 2 == 0:
        oven_numbers.append(num)
oven_numbers.sort(reverse=True)
for num1 in numbers:
    if num1 % 2 != 0:
        new_list.append(num1)
    else:
        new_list.append(oven_numbers.pop(0))
print(f'Список после сортировки: {new_list}')
