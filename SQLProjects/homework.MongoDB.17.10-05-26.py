#task1 Тестовая коллекция в mongo atlas  sample_mflix.theaters.
# Найти все кинотеатры в Калифорнии и посчитать их количество.

from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
result = client['sample_mflix']['theaters'].aggregate([
    {
        '$match': {
            'location.address.city': 'California'
        }
    }, {
        '$count': 'city_California'
    }
])

#task2 Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews.
# Найти недвижимость с самым большим количеством спален (bedrooms) и напишите ее название.

from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$sort': {
            'bedrooms': -1
        }
    }, {
        '$limit': 1
    }, {
        '$project': {
            'name': 1
        }
    }
])

#task3 Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews.
# Найти недвижимость с самым высоким рейтингом  review_scores_rating при минимальном количестве отзывов 50 (number_of_reviews) и напишите ее название.

from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'number_of_reviews': {
                '$gte': 50
            }
        }
    }, {
        '$sort': {
            'review_scores.review_scores_rating': -1
        }
    }, {
        '$limit': 1
    }, {
        '$project': {
            'name': 1
        }
    }
])

