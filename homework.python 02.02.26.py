#task1
num = int(input('Введите число: '))
for c in range(1, num + 1):
    for j in range(1, num +1):
        print(c * j, end ='\t')
    print()
#task2
n = int(input('Введите число: '))
result = 0
for c in range(1, n + 1):
    result += 1
    for j in range(1, result):
        print(j, end=' ')
    print(c)
#task3
string = input('Введите строку: ')
result = ''
for c in string:
    if c not in result:
        result += c
print(f'Результат: {result}')


