#task1
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третее число: '))
if num1 > num2 > num3:
    print(f'Числа в порядке возраствния: {num3}, {num2}, {num1}')
elif num2 > num1 > num3:
    print(f'Числа в порядке возраствния: {num3}, {num1}, {num2}')
elif num3 > num2 > num1:
    print(f'Числа в порядке возраствния: {num1}, {num2}, {num3}')
elif num1 > num3 > num2:
    print(f'Числа в порядке возраствния: {num2}, {num3}, {num1}')
elif num3 > num1 > num2:
    print(f'Числа в порядке возраствния: {num2}, {num1}, {num3}')
else:
     print(f'Числа в порядке возраствния: {num1}, {num3}, {num2}')
#task2
year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Год являеться высокостным.')
else:
    print('Год являеться не высокстным.')

