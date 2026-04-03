#task1 Повторения букв.
# Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.
# Данные:
# text = "Programming is fun!"
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

from collections import Counter
text = "Programming is fun!"
# new_text = ''
# for c in text.lower():
#     if c.isalpha():
#         new_text += c
# x = Counter(new_text)
# print(dict(x))

def count_letters(t):
    new_text = ''
    for c in t.lower():
        if c.isalpha():
            new_text += c
    x = Counter(new_text)
    return dict(x)
print(count_letters(text))

#task2 Группировка студентов по классам.
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

from collections import defaultdict
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
new_dict = defaultdict(list)
for student in students:
    new_dict[student[0]].append(student[1])
print(dict(new_dict))