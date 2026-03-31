#task1 Оценки текстом.
# Напишите программу, которая преобразует список оценок по системе от 1 до 5 в текстовое представление. Нужно сохранить в списках числовой результат и текстовое представление. Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно".
# Данные:
# grades = [5, 3, 4, 2, 1, 5, 3]
# Пример вывода:
# [[5, 'отлично'], [3, 'хорошо'], [4, 'хорошо'], [2, 'неудовлетворительно'], [1, 'неудовлетворительно'], [5, 'отлично'], [3, 'хорошо']]

grades = [5, 3, 4, 2, 1, 5, 3]
print([[grade, 'отлично'] if grade == 5 else ([grade, 'хорошо'] if grade == 3 or grade == 4 else [grade, 'неудовлетворительно']) for grade in grades]) #через list comprehension

labels = ['отлично' if grade == 5 else ('хорошо' if grade == 3 or grade == 4 else 'неудовлетворительно') for grade in grades] #через zip()
result = [list(res) for res in zip(grades, labels)]
print(result)

#task2 Правильные скобки.
# Напишите программу, которая принимает строку, содержащую любые виды скобок — круглые (), квадратные [] и фигурные {}.
# Необходимо проверить, правильно ли они расставлены. Скобки считаются правильно расставленными, если:
# Каждая открывающая скобка имеет соответствующую закрывающую.
# Скобки закрываются в правильном порядке.
# Пример данных:
# string = "({[}])"
# Пример вывода:
# Скобки: ({[}])
# Валидны: False
# Скобки: ([({}()){}])
# Валидны: True

string = "({[}])"
open_parentheses = '({['
close_parentheses = ')}]'
stack = []
x = 0
is_valid = True
for c in string:
    if c in open_parentheses:
        stack.append(c)
    elif c in close_parentheses:
        idx = close_parentheses.index(c)
        if not stack:
            is_valid = False
            break
        else:
            is_valid = (idx == open_parentheses.index(stack.pop()))
            if not is_valid:
                break
print(f'Скобки: {string}')
print(f"Валидны: {is_valid and len(stack) == 0}")

