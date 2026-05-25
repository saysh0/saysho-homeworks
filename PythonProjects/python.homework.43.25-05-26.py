# task1 Добавление товаров.
# Создайте программу, которая подключается к MongoDB и:
# 1.выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
# 2.очищает коллекцию перед началом
# 3.добавляет 3 товара с полями: name, price, stock
# 4.выводит сообщение о количестве добавленных товаров.

#task2 Увеличение цен.
# Продолжите предыдущую задачу. Теперь программа должна:
# 1.увеличить цену всех товаров на 20%
# 2.вывести количество обновлённых записей
# 3.затем вывести список всех товаров с новыми ценами

products = [
 {"name": "Notebook", "price": 599, "stock": 67},
 {"name": "GamingPC", "price": 2000, "stock": 3},
 {"name": "APHONE", "price": 1000, "stock": 52},
]

from cfg_to_connect import cfg
from pymongo import MongoClient
class Mongodb:
    def __init__(self, client):
        self.client = MongoClient(client)
        self.db = self.client['ich_edit']
        self.collection = None

    def client_close(self):
        self.client.close()
        return 'Done!'  # для себя

    def conn_collection(self, collection_name):
        self.collection = self.db[collection_name]
        return 'Done!'  # для себя

    def delete_all_from_collection(self):
        self.collection.delete_many({})
        return 'Done!'  # для себя

    def insert_many_to_collection(self, data):
        len_data = len(data)
        self.collection.insert_many(data)
        print('Done!') #для себя
        return len_data

    def increase_all_price_20_precent(self):
        res = self.collection.update_many({}, {'$mul': {'price': 1.2}})
        print('Done!') # для себя
        return res.matched_count

    def all_updated_in_collection(self):
        return self.collection.find({'price': {'$exists': True}})

user1 = Mongodb(cfg)
print(user1.conn_collection('121225ptm_NikitaO'))
print(user1.delete_all_from_collection())
print(f"{user1.insert_many_to_collection(products)} products inserted.")
print(f"Price updated for {user1.increase_all_price_20_precent()} products.")
print('Updated products:')
for row in user1.all_updated_in_collection():
    print(f'- {row["name"]} - ${row["price"]}')
print(user1.client_close())
