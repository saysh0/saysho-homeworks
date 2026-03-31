#task 1
first_value = int(input('Enter first value: '))
second_value = int(input('Enter second value: '))
print(f'and:{first_value > 0 and second_value > 0}')
print(f'or:{first_value > 0 or second_value > 0}')
print(f'not:{not first_value}')
print(f'equal:{first_value == second_value}')
print(f'not equal:{first_value != second_value}')
#task 2
light = str(input('Включен ли свет?: '))
window = str(input('Открыто ли окно?: '))
if light == 'Да':
    print('Свет включен?: True')
if light == 'Нет':
    print('Свет включен?: False')
if window == 'Да':
    print('Окно открыто?: True')
if window == 'Нет':
    print('Окно открыто?: False')
print(f'Оба условия выполнены?: {light == "Да" and window == "Да"}')
print(f'Хотябы одно условие выполнено?: {light == "Да" or window == "Да"}')
#task 3
used_internet = int(input('Введите использованные (мб) интернета: '))
based_internet_value = 30
one_month_internet_over_500mb_value = 0.2
if used_internet > 500:
    used_internet -= 500
    used_internet *= one_month_internet_over_500mb_value
    price_pay = used_internet + based_internet_value
    print(f'Общая стоимость:{price_pay}')
