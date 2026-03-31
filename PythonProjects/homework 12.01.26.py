# task1
x = input('Введите четырехзначное число:')
a, b, c, d = x[0], x[1], x[2], x[3]
y = int(a) + int(b) + int(c) + int(d)
print('Сумма цифр числа:', + y)
# #task2
firs_number = input('Введите первое число:')
second_number = input('Введите второе число:')
print(f'Результат: {int(firs_number) * int(second_number)}-{firs_number}-{second_number}')
# task3.1
first_number_task_3_1 = input('Введите первое число:')
second_number_task_3_1 = input('Введите второе число:')
first_number_task_3_1 = int(first_number_task_3_1)
second_number_task_3_1 = int(second_number_task_3_1)
h = first_number_task_3_1 / second_number_task_3_1
h = int(h)
h *= second_number_task_3_1
first_number_task_3_1 -= h
print(first_number_task_3_1)
# task3.2
firs_number_task_3_2 = input('Введите первое число:')
second_number_task_3_2 = input('Введите второе число:')
f = (int(firs_number_task_3_2) / int(second_number_task_3_2))
print(int(f))
