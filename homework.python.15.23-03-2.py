#task1 Одно слово.
# Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
for i in range(len(text_list)):
    if ' ' in text_list[i]:
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()
print(f'Обработанный список: {text_list}')

#task2 Обновление цен товаров.
# Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
# Данные:
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# Пример вывода:
# Введите скидку (в процентах): 17
# Товар          Старая цена    Новая цена
# Laptop            1200.00$       996.00$
# Mouse                25.00$         20.75$
# Keyboard           75.00$         62.25$
# Monitor            200.00$       166.00$

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
sale_amount = int(input('Введите скидку (в процентах): '))
concept = ['Товар', 'Стартовая цена', 'Новая цена']
print(f'{concept[0]:15}{concept[1]:>15}{concept[2]:>15}')
for product, price in products:
    new_price = price - (price / 100 * sale_amount)
    print(f'{product:15} {price:>13.2f}$ {new_price:>13.2f}$')