#task1 Создание базы.
# Напишите программу, которая:
# 1создаёт базу данных notes_app_<your_group>_<your_full_name>
# 2выбирает эту базу через USE notes_app
# 3выводит сообщение о результате

#task2 Добавление заметок.
# Продолжите предыдущую программу:
# создайте таблицу notes с полями: id, title, content
# 1вставьте одну заметку в таблицу
# 2выполните commit() после вставки
# 3выведите все заметки используя DictCursor

import pymysql
config = {
        'host': 'ich-edit.edu.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'cursorclass': pymysql.cursors.DictCursor
      }
#
# conn = pymysql.connect(**config)
# cursor = conn.cursor()
# cursor.execute('USE notes_app_121225_ptm_NikitaOrmandzhan')
#
# try:
#     cursor.execute('CREATE DATABASE notes_app_121225_ptm_NikitaOrmandzhan')
# except pymysql.err.ProgrammingError:
#     print("Database 'notes_app' already exists.")
# except Exception as e:
#     print(f'Ошибка:{e}')
# else:
#     print("Database 'notes_app' created.")
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS notes (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#                                                    title varchar(100) NOT NULL,
#                                                    content varchar(100) NOT NULL)""")
#
# # cursor.execute("""INSERT INTO notes (title, content) VALUES ('Shopping', 'list')""")
# cursor.execute('SELECT * FROM notes')
# print("Notes added: ", end='')
# for item in cursor.fetchall():
#     item_keys = list(item.keys())
#     column1 = item_keys[1]
#     column2 = item_keys[2]
#     print(item[column1], item[column2])
# conn.commit()

class DBUsage:
    def __init__(self, config):
        self.conn = pymysql.connect(**config)

    def conn_close(self):
        self.conn.close()

    def conn_commit(self):
        self.conn.commit()

    def conn_rollback(self):
        self.conn.rollback()

    def execute_sql(self, sql,  params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            if cursor.description:
                return cursor.fetchall()

    def create_db(self, name):
        safe_name = name.replace('`', '')
        with self.conn.cursor() as cursor:
            cursor.execute(f'CREATE DATABASE `{safe_name}`')
            cursor.execute(f'USE `{safe_name}`')

    def create_table(self, table_name, param=None):
        if not param:
            raise ValueError("Необходимо указать хотя бы одну колонку в param (например: 'id INT, name VARCHAR(100)')")
        with self.conn.cursor() as cursor:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS `{table_name}` ({param})""")

    def insert_data(self, table_name, column, param):
        values = [value.strip() for value in param.split(',')]
        inpt = ','.join(['%s'] * len(values))
        with self.conn.cursor() as cursor:
            cursor.execute(f"""INSERT INTO `{table_name}` ({column}) VALUES ({inpt}""", values)


db1 = DBUsage(config)
try:
    db1.create_db('notes_app_121225_ptm_NikitaOrmandzhan')
except pymysql.err.ProgrammingError:
    print("Database 'notes_app' already exists.")
except Exception as e:
    print(f'Ошибка:{e}')
else:
    print("Database 'notes_app' created.")

table_column = "id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, title varchar(100) NOT NULL, content varchar(100) NOT NULL"
db1.create_table('notes', table_column)
db1.insert_data('notes', 'title, content', 'Shopping, list')

res = db1.execute_sql('SELECT * FROM notes')
print("Notes added: ", end='')
for item in res:
    item_keys = list(item.keys())
    column1 = item_keys[1]
    column2 = item_keys[2]
    print(item[column1], item[column2])
db1.conn_commit()
db1.conn_close()