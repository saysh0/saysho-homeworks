#task1
symbol = input('Введите символ: ')
print(f'Код Unicode: {ord(symbol)}')
is_ascii = ord(symbol) <= 127
print(f'ASCII: {is_ascii}')
#task2
stroka = str(input('Введите строку:'))
index1 = int(input('Введите начальный индекс: '))
index2 = int(input('Введите конечный индекс: '))
podstroka = stroka[index1 : index2]
if len(podstroka) < index2:
    nehvataet = index2 - len(podstroka)
    podstroka += nehvataet * '_'
print(f'Подстрока: {podstroka}')
#task3
stroka = str(input('Введите строку: '))
symbol = str(input('Введите символ: '))
lenght_stroka = 0
symbol_count = 0
while lenght_stroka < len(stroka):
    if stroka[lenght_stroka] == symbol:
        symbol_count += 1
    lenght_stroka += 1
print(f'Символ {symbol} встречаеться {symbol_count} раз(а)')
#task4
stroka = str(input('Введите строку: '))
result = ''
num = len(stroka) -1
while num > 0:
    a = stroka[num]
    if not a.isdigit():
        result += a
    num -= 1
print(f'Результат: {result}')

