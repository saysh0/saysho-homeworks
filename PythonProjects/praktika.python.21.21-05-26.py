#task1 Создание книжного магазина.
# Создайте новую базу данных под названием bookstore.
# После этого выполните проверку: если база данных успешно создана (или уже существует), выведите сообщение:
# Database 'bookstore' created or already exists.

#task2 Создание таблиц для магазина.
# Расширьте предыдущую программу: после создания базы данных bookstore, создайте в ней две таблицы:
# ● books — для хранения информации о книгах;
# ● users — для регистрации клиентов.
# После создания таблиц выведите список всех таблиц в текущей базе.
# Пример вывода:
# Tables in 'bookstore':
# - books
# - users

import pymysql
from collections.abc import Iterable
import re

class Database:
    def __init__(self, connection):
        self.connection = pymysql.connect(**connection)


    def execute(self, query, params=None):
        self._params_check(params)

        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description:
                return cursor.fetchall()

        return None


    def commit(self):
        return self.connection.commit()

    def rollback(self):
        return self.connection.rollback()


    def executemany(self, query, params=None):
        self._params_check(params)

        with self.connection.cursor() as cursor:
            cursor.executemany(query, params)
            self.commit()


    def close(self):
        return self.connection.close()


    def create_and_use_db(self, name: str):
        self._validator(name)
        self.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
        self.execute(f"USE {name}")


    def create_table(self, name, params):
        self._validator(name)
        self.execute(f"CREATE TABLE IF NOT EXISTS {name} ({params})")


    def insert(self, name, data:dict):
        self._validator(name)

        if not isinstance(data, dict):
            raise ValueError("Должно быть словарем")

        for column in data:
            self._validator(column)

        columns = ", ".join(data.keys())
        values = tuple(data.values())
        placeholders = ", ".join(["%s"] * len(data))

        self.execute(f"INSERT INTO {name} ({columns}) VALUES ({placeholders})", values)



    def insert_many(self, name, rows):
        self._validator(name)
        self._validate_rows(rows)

        columns = ", ".join(rows[0].keys())
        values = [tuple(row.values()) for row in rows]
        placeholders = ", ".join(["%s"] * len(rows[0]))

        self.executemany(f"INSERT INTO {name} ({columns}) VALUES ({placeholders})", values)

    def get_all_tables(self):
        return self.execute("SHOW TABLES")


    @staticmethod
    def _params_check(params):
        if params is None:
            return

        if not isinstance(params, Iterable) or isinstance(params, str):
            raise ValueError("Должно быть итерируемым и не строкой")


    @staticmethod
    def _validator(name):
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            raise ValueError("Нельзя такой формат!!!")


    def _validate_rows(self, rows):
        if not rows:
            raise ValueError("rows пустой")

        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("Должно быть словарем")

            for column in row:
                self._validator(column)

config = {
        'host': 'ich-edit.edu.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'cursorclass': pymysql.cursors.DictCursor
      }

BookStore = Database(config)

try:
    BookStore.create_and_use_db("bookstore_Nikita")
except Exception as e:
    print("Error to use or create db:", e)
else:
    print("Database 'bookstore' created or already exists.")
books_table_config = """id INT PRIMARY KEY AUTO_INCREMENT,
                        title VARCHAR(100) NOT NULL,
                        author VARCHAR(100),
                        price DECIMAL(10, 2) NOT NULL,
                        quantity INT NOT NULL"""
users_table_config = """id INT PRIMARY KEY AUTO_INCREMENT,
                        login VARCHAR(20) NOT NULL UNIQUE,
                        password VARCHAR(20) NOT NULL,
                        balance decimal(10,2) NOT NULL"""
try:
    BookStore.create_table("books", books_table_config)
    BookStore.create_table("users", users_table_config)
except Exception as e:
    print("Error to use or create db:", e)
else:
    print("Database 'bookstore' created or already exists.")

print(BookStore.get_all_tables())