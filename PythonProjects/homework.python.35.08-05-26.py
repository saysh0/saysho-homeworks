#task1 Счётчик экземпляров.
# Создайте класс User, представляющий пользователя.
# При создании должны указываться логин (username) и пароль (password).
# У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
# При каждом создании нового объекта User, счётчик должен увеличиваться.
# Добавьте метод get_total(), возвращающий количество пользователей.
# Проверьте, что счётчик работает.

# class User:
#     total_users = 0
#     def __init__(self, username: str, password: str | int):
#         self.username = username
#         self.password = password
#         User.total_users += 1
#
#     def get_total(self):
#         return self.total_users
#
#
# usr1 = User("user1", "cheremsha10")
# usr2 = User("user2", "cheremsha20")
# usr3 = User("user3", "cheremsha30")
# print(f"Total users: {usr1.get_total()}")

#task2 Проверка данных пользователя.
# Доработайте класс User.
# Добавьте валидации полей при создании.
# Имя должно быть непустой строкой.
# Пароль должен быть строкой длиной не менее 5 символов.
# Если данные некорректны — выбрасывайте ValueError.
# Добавьте строковое представление объекта.
# Проверьте работу класса с разными значениями.

class User:
    total_users = 0
    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1
        if not username:
            raise ValueError('Field username is empty!')
        if not password:
            raise ValueError('Field password is empty!')
        if len(password) <= 5:
            raise ValueError('Field password is too short!')
        if not isinstance(password, str):
            raise ValueError('Filed password is invalid!')

    def get_total(self):
        return self.total_users

    def __str__(self):
        return f"Пользователь: {self.username}, пароль: {self.password}"


usr1 = User("user1", "cheremsha10")
print(usr1)
try:
    usr2 = User("", "cheremsha20")
    print(usr2)
except ValueError as e:
    print(e)

try:
    usr3 = User("user3", "")
    print(usr3)
except ValueError as e:
    print(e)

try:
    usr4 = User("user4", "123")
    print(usr4)
except ValueError as e:
    print(e)