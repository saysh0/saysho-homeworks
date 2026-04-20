#task1 Создайте генератор, который генерирует последовательность Фибоначчи бесконечно, возвращая по одному числу за раз.
# Последовательность Фибоначчи — это ряд чисел, где каждое следующее число равно сумме двух предыдущих.
# Начинается с 0 и 1.
# Пример вывода:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(20 * '-')
gen1 = fibonacci()
for n, i in enumerate(gen1):
    print(i, end='\n')
    if n >= 10:
        break
print(20 * '-')
for n, i in enumerate(gen1):
    print(i, end='\n')
    if n >= 10:
        break

#task2 Генератор уникальных элементов
# Создайте генератор, который принимает список элементов и выдаёт только уникальные значения, сохраняя порядок их появления в исходном списке.
# Данные:
# data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
# Пример вывода:
# 3
# 1
# 2
# 4
# 5
# 6
# 7
# 8

#BAD при работе с большим файлом съест много памяти
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
def unic_elements(lst):
    unique = [unique for i, unique in enumerate(lst) if unique not in lst[:i]]
    yield from unique


for item in unic_elements(data):
    print(item)
print(20 * '-')

def unic_elements_v2(lst):
    new_set = set()
    for item in lst:
        if item not in new_set:
            yield item
            new_set.add(item)


gen2 = unic_elements_v2(data)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(20 *'-')
for item in unic_elements_v2(data):
    print(item)
