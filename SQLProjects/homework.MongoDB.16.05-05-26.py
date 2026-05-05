#task1 Найдите средний возраст из коллекции ich.US_Adult_Income.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
result = client['ich']['US_Adult_Income'].aggregate([
    {
        '$group': {
            '_id': None,
            'avgAge': {
                '$avg': '$age'
            }
        }
    }
])

#task2 Поменяв подключение к базе данных, создать коллекцию orders_NAME (для уникальности - добавим ваше имя в название) со свойствами id, customer, product, amount, city, используя следующие данные:
# 1 Olga Apple 15.55 Berlin
# 2 Anna Apple 10.05 Madrid
# 3 Olga Kiwi 9.6 Berlin
# 4 Anton Apple 20 Roma
# 5 Olga Banana 8 Madrid
# 6 Petr Orange 18.3 Paris

db.orders.insertMany([
  { id: 1, customer: 'Olga', product: 'Apple', amount: 15.55, city: 'Berlin' },
  { id: 2, customer: 'Anna', product: 'Apple', amount: 10.05, city: 'Madrid' },
  { id: 3, customer: 'Olga', product: 'Kiwi', amount: 9.6, city: 'Berlin' },
  { id: 4, customer: 'Anton', product: 'Apple', amount: 20, city: 'Roma' },
  { id: 5, customer: 'Olga', product: 'Banana', amount: 8, city: 'Madrid' },
  { id: 6, customer: 'Petr', product: 'Orange', amount: 18.3, city: 'Paris' }
])


#task3Найти сколько всего было совершено покупок.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Nikita'].aggregate([
    {
        '$count': 'all_orders'
    }
])

#task4 Найти сколько всего раз были куплены яблоки.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Nikita'].aggregate([
    {
        '$match': {
            'product': 'Apple'
        }
    }, {
        '$count': 'Apple_orders'
    }
])

#task5 Вывести идентификаторы трех самые дорогих покупок.

from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
filter={}
project={
    'id': 1
}
sort=list({
    'amount': -1
}.items())
limit=3

result = client['ich_edit']['orders_Nikita'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

#task6 Найти сколько всего покупок было совершено в Берлине.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
filter={
    'city': 'Berlin'
}

result = client['ich_edit']['orders_Nikita'].find(
  filter=filter
)

#task7 Найти количество покупок яблок в городах Берлин и Мадрид.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Nikita'].aggregate([
    {
        '$match': {
            'city': {
                '$in': [
                    'Berlin', 'Madrid'
                ]
            }
        }
    }, {
        '$match': {
            'product': 'Apple'
        }
    }, {
        '$group': {
            '_id': None,
            'Apple_amount': {
                '$sum': '$amount'
            }
        }
    }
])

#task8 Найти сколько было потрачено каждым покупателем.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Nikita'].aggregate([
    {
        '$group': {
            '_id': '$customer',
            'total_amount': {
                '$sum': '$amount'
            }
        }
    }
])

#task9 Найти в каких городах совершала покупки Ольга.
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit')
result = client['ich_edit']['orders_Nikita'].aggregate([
    {
        '$match': {
            'customer': 'Olga'
        }
    }, {
        '$group': {
            '_id': '$city'
        }
    }
])

