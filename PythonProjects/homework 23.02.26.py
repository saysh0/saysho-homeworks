#task1 Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

text = "My number is 123-456-789"
text_remake = ''
for c in text:
    if c.isdigit():
        print(c.replace(c, '*'), end='')
    else:
        print(c, end='')

#task2 Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

text = "Programming in python"
print(f'Строка: {text}')
lower_text = text.lower()
repeated_symbol = ''
for c in lower_text:
    if c not in repeated_symbol:
        repeated_symbol += c
        count = lower_text.count(c)
        if count > 1:
            print(f"Символ '{c}' встречается {count} раз(а)")

#task3 Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
splited_text = text.split()
new_string = ''
for i in splited_text:
    if i.isdigit() or ('.' in i and not i.endswith('.')):
        i = str(float(i) * 10)
    new_string += (i + ' ')
print(new_string)

