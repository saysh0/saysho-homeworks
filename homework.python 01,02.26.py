import random
#task1
num = int(input('Веведите число: '))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print(f'Сумма цифр: {sum_digits}')
#task2
num = int(input('Введите число: '))
reverse = 0
num2 = num
while num2 > 0:
    reverse = reverse * 10 + num2 % 10
    print(reverse) #делал пометки для себя
    num2 //= 10
print(reverse) #делал пометки для себя
if num == reverse:
    print(f"Число {num} является палиндромом.")
else:
    print(f"Число {num} не является палиндромом.")
#task3
num = random.randint(1, 100)
max_attempts = 10
attempt = 0
print(num)
print('Угадайте число от 1 до 100. Увас 10 попыток.')
while attempt < max_attempts:
    user_num = int(input('Ваше предложение: '))
    attempt += 1
    if attempt == 10:
        print('Вы использовали все попытки. Повезет в следующий раз!')
    elif num > user_num :
        print('Загаданое число больше вашего')
    elif num < user_num:
        print('Загаданое число меньше вашего')
    elif attempt == 1:
        print(f'Отличная интуиция! Вы угадали число {num} за {attempt} попыток.')
        break
    else:
        print(f'Поздравляем! Вы угадали число {num} за {attempt} попыток. Отличный результат!')


