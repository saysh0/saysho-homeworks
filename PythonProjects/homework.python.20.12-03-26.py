#task1 Простое число.
# Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и возвращает булевый результат.
# Данные:
# n = 17
# Пример вывода:
# Число 17 является простым

def prime_number(n):
    is_prime_number = True if n / n == 1 and n % 2 == 1 else False
    return f'Число {n} является простым: {is_prime_number}'
print(prime_number(17))

#task2 Фильтрация чисел по чётности.
# Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел, возвращая только те, которые соответствуют фильтру.
# Пример вызова:
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))
# Пример вывода:
# [2, 4, 6]
# [15, 25]
# Некорректный фильтр

def filter_numbers(filter_type, *numbers):
    if filter_type == "even":
        return [num for num in numbers if num % 2 == 0]
    elif filter_type == "odd":
        return [num for num in numbers if num % 2 != 0]
    else:
        return "Некорректный фильтр"
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

#task3 Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи повторяются, используется значение из последнего словаря.
# Данные:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = {"d": 5}
# Пример вызова:
# print(merge_dicts(dict1, dict2, dict3))
# Пример вывода:
# {'a': 1, 'b': 3, 'c': 4, 'd': 5}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

def dict_join(*args):
    new_dict = {}
    for i in args:
        new_dict.update(i)
    return new_dict
print(dict_join(dict1, dict2, dict3))

