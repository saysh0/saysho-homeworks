#task1 Из коллекции customers выяснить из какого города "Sven Ottlieb".
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'ContactName': 'Sven Ottlieb'
}
project={
    '_id': 0,
    'ContactName': 1,
    'City': 1
}
result = client['ich']['customers'].find(
  filter=filter,
  projection=project
)

#task2 Из коллекции ich.US_Adult_Income найти возраст самого взрослого человека.
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={}
sort=list({
    'age': -1
}.items())
limit=1

result = client['ich']['US_Adult_Income'].find(
  filter=filter,
  sort=sort,
  limit=limit
)

#task3 Из 2 задачи выясните, сколько человек имеют такой же возраст.
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'age': 90
}

result = client['ich']['US_Adult_Income'].find(
  filter=filter
)

#task4 Найти _id ObjectId документа, в котором education " IT-career-hub".
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'education': ' IT-career-hub'
}
project={
    'education': 1
}

result = client['ich']['US_Adult_Income'].find(
  filter=filter,
  projection=project
)

#task5 Выяснить количество людей в возрасте между 20 и 30 годами.
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'age': {
        '$gte': 20,
        '$lte': 30
    }
}
sort=list({
    'age': 1
}.items())

result = client['ich']['US_Adult_Income'].find(
  filter=filter,
  sort=sort
)

