import math
#task1
num1 = float(input('Enter a number: '))
if num1 > 0:
    print(f'Округленное значение: {math.floor(num1 + 0.5)}')
else:
    print(f'Округленное значение: {math.ceil(num1 - 0.5)}')
#task2
x = int(input('Enter katet 1: '))
y = int(input('Enter katet 2: '))
print(f'Длинна гипотенузы: {math.sqrt(pow(x, 2) + pow(y, 2))}')


