#task1 Среднее время выполнения.
# Создайте декоратор measure_time, который измеряет и выводит среднее время выполнения функции за 5 вызовов.
# Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.
# Пример применения:
# @measure_time
# def compute():
# total = 0
# for i in range(10_000_000):
# total += 1
# return total
# Пример вывода:
# Среднее время выполнения для 5 вызовов: 0.21 секунд
# Результат: 49999995000000

def measure_time(func):
    def wrapper(*args, **kwargs):
        import time
        avg_time = 0
        for _ in range(5):
            start = time.perf_counter()
            func()
            end = time.perf_counter()
            avg_time += end - start
        return f'Среднее время выполнения для 5 функций: {round(avg_time / 5, 2)}\nРезультат: {func()}'
    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += 1
    return total

print(compute())

#task2 Среднее время выполнения с количеством вызовов.
# Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
# Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.
# Пример применения:
# @measure_time(10)
# def compute():
# total = 0
# for i in range(10_000_008):
# total += 1
# return total
# Пример вывода:
# Среднее время выполнения для 10 вызовов: 0.21 секунд
# Результат: 49999995000000

def measure_time(repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            avg_time = 0
            for _ in range(repeats):
                start = time.perf_counter()
                func()
                end = time.perf_counter()
                avg_time += end - start
            return f'Среднее время выполнения для {repeats} функций: {round(avg_time / repeats, 2)}\nРезультат: {func()}'
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += 1
    return total

print(compute())