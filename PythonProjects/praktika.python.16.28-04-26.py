#task1 Ограничение длины строки.
# Создайте декоратор limit_output(max_len), который обрезает строку, возвращаемую функцией, до max_len
# символов.
# Если строка длиннее, то она обрезается до выбранного лимита и завершается троеточием ..., входящим в этот
# лимит.
# Пример применения:
# @limit_output
# def get_text():
#  return "Это очень длинный текст, который нужно обрезать."
# Пример вывода:
# Это очень длинный...
import functools


# def max_len(original_func, lenght=17):
#     def wrapper():
#         text = original_func()
#         if len(text) > lenght:
#             return f'{text[:lenght]}...'
#     return wrapper
#
# @max_len
# def get_text():
#     return "Это очень длинный текст, который нужно обрезать."
# print(get_text())

#task2 Ограничение с указанием длины строки.
# Доработайте декоратор limit_output,чтобы он принимал параметр max_len — максимальная длина строки.
# Пример применения:
# @limit_output(26)
# def get_text():
#  return "Это очень длинный текст, который нужно обрезать."
# Пример вывода:
# Это очень длинный текст...

# def limit_output(limit=17):
#     def decorator(original_func):
#         def wrapper():
#             text = original_func()
#             if len(text) > limit:
#                 return f'{text[:limit]}...'
#         return wrapper
#     return decorator
#
# @limit_output(26)
# def get_text():
#     return "Это очень длинный текст, который нужно обрезать."
# print(get_text())

#task3 Кеширование результатов.
# Создайте декоратор cache, который сохраняет результат вызова функции для каждого набора аргументов.
# Если функция вызывается повторно с теми же аргументами — возвращается сохранённый результат.
# Пример применения:
# @cache
# def multiply(a, b):
#  print(f"Вычисляем {a} * {b}: ")
#  return a * b
# Пример вывода:
# Вычисляем 2 * 3:
# 6
# Результат из кеша:
# 6
# Вычисляем 4 * 5:
# 20
# Результат из кеша:
# 6

# def cache(original_func):
#     cache_dict = {}
#     def wrapper(*args):
#         if args not in cache_dict:
#             cache_dict[args] = original_func(*args)
#         return cache_dict[args]
#     return wrapper
#
# import time
# @cache
# def multiply(a, b):
#     time.sleep(10)
#     return a * b
# print(multiply(2, 3))
# print(multiply(2, 3))
# print(multiply(4, 5))
# print(multiply(4, 5))

#task4 Кеш с ограничением по размеру.
# Доработайте декоратор cache, чтобы он:
# ● Принимал параметр max_size, ограничивающий количество сохранённых записей.
# ● При превышении max_size — удалял самую старую запись из кеша.
# Пример применения:
# @cache(max_size=2)
# def multiply(a, b):
#  print(f"Вычисляем {a} * {b}: ")
#  return a * b
# Пример вывода:
# Вычисляем 2 * 3:
# 6
# Результат из кеша:
# 6
# Вычисляем 4 * 5:
# 20
# Вычисляем 6 * 7:
# 42
# Вычисляем 2 * 3:
# 6

def cache(max_size=None):
    def decorator(original_func):
        from collections import OrderedDict
        cache_dict = OrderedDict()
        def wrapper(*args):
            if args in cache_dict:
                cache_dict.move_to_end(args)
                return cache_dict[args]
            if max_size is not None and len(cache_dict) >= max_size:
                cache_dict.popitem(last=False)
            result = original_func(*args)
            cache_dict[args] = result
            return result
        return wrapper
    return decorator

import time
@cache(max_size=2)
def multiply(a, b):
    time.sleep(3)
    return a * b
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(6, 7))
print(multiply(2, 3))