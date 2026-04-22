#task1 Коллекция imdb : Используя оператор $size , найдите фильмы, написанные 3 сценаристами (writers) и снятые 2 режиссерами (directors)
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'type': 'movie',
    'directors': {
        '$size': 2
    },
    'writers': {
        '$size': 3
    }
}

result = client['ich']['imdb'].find(
  filter=filter
)

#task2 Коллекция bookings: Найдите адрес нахождения автомобиля с vin WME4530421Y135045 по самой последней дате (и времени) final_date

from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'vin': 'WME4530421Y135045'
}
project={
    'final_date': 1,
    'vin': 1,
    'final_address': 1
}
sort=list({
    'final_date': -1
}.items())
limit=1

result = client['ich']['bookings'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

#task3 Коллекция bookings: подсчитайте, у скольких автомобилей при окончании аренды закончилось топливо (final_fuel)

from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'final_fuel': 0
}

result = client['ich']['bookings'].find(
  filter=filter
)
#30 машин

#task4 Коллекция bookings: найдите номерной знак и vin номер авто, с самым большим километражом (distance)

from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={}
project={
    'plate': 1,
    'vin': 1,
    'distance': 1
}
sort=list({
    'distance': -1
}.items())
limit=1

result = client['ich']['bookings'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

#task5 Коллекция imdb. Найдите фильм с участием "Brad Pitt" с самым высоким рейтингом (imdb.rating)

from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'imdb.rating': {
        '$gt': 1
    },
    'cast': 'Brad Pitt'
}
sort=list({
    'imdb.rating': -1
}.items())
limit=1

result = client['ich']['imdb'].find(
  filter=filter,
  sort=sort,
  limit=limit
)