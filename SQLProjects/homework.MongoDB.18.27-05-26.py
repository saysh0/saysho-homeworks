#task1 Из коллекции sample_airbnb.listingsAndReviews найдите среднюю цену за сутки проживания на Гавайских островах.
# Островов несколько, поэтому либо используем {'address.location': {$geoWithin: { $centerSphere ….
# Либо перечисляем все возможные острова в поле market
# Подсказка - нам понадобится 2 этапа агрегации : $match и $group

from pymongo import MongoClient
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'address.market': {
                '$in': [
                    'Oahu', 'Maui', 'The Big Island', 'Kauai'
                ]
            }
        }
    }, {
        '$group': {
            '_id': None,
            'avg_price': {
                '$avg': '$price'
            }
        }
    }
])

#task2 Подсчитайте в коллекции sample_mflix.movies, сколько фильмов имеют imdb рейтинг выше 8 и выходили в период с 2015
#до 2023 года (используем year). Какой из них имеет самый высокий рейтинг ?

from pymongo import MongoClient
filter={
    'imdb.rating': {
        '$gt': 8
    },
    'year': {
        '$gte': 2015,
        '$lte': 2023
    }
}

result = client['sample_mflix']['movies'].find(
  filter=filter
)

from pymongo import MongoClient
filter={
    'imdb.rating': {
        '$gt': 8
    },
    'year': {
        '$gte': 2015,
        '$lte': 2023
    }
}
sort=list({
    'imdb.rating': -1
}.items())

result = client['sample_mflix']['movies'].find(
  filter=filter,
  sort=sort
)
#_id: {"$oid": "573a13f0f29313caabdda542"}
