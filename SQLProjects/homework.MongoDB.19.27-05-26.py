#task1 Найдите трек с наивысшими показателями  Danceability и Energy.

from pymongo import MongoClient
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={}
sort=list({
    'Danceability': -1,
    'Energy': -1
}.items())
limit=1

result = client['ich']['Spotify_Youtube'].find(
  filter=filter,
  sort=sort,
  limit=limit
)

#task2 У какого трека (но не compilation) самая большая длительность?

from pymongo import MongoClient
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'Album_type': {
        '$ne': 'compilation'
    }
}
sort=list({
    'Duration_ms': -1
}.items())
limit=1

result = client['ich']['Spotify_Youtube'].find(
  filter=filter,
  sort=sort,
  limit=limit
)

#task3 В каком одном альбоме самое большее количество треков?

from pymongo import MongoClient
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
result = client['ich']['Spotify_Youtube'].aggregate([
    {
        '$group': {
            '_id': '$Album',
            'total_tracks': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'total_tracks': -1
        }
    }, {
        '$limit': 1
    }
])

#task4 Сколько просмотров видео на youtube у трека с самым высоким количеством прослушиваний на spotify (Stream)?

from pymongo import MongoClient
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={}
project={
    'Views': 1
}
sort=list({
    'Stream': -1
}.items())
limit=1

result = client['ich']['Spotify_Youtube'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

#task5 Экспортируйте 20 самых популярных (прослушивания или просмотры) треков по версиям youtube и spotify и
#импортируйте в базу ich_edit их с именами top20youtube и top20spotify, и добавьте им свои имена для уникальности.

from pymongo import MongoClient #Youtube
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
result = client['ich']['Spotify_Youtube'].aggregate([
    {
        '$sort': {
            'Views': -1
        }
    }, {
        '$limit': 20
    }, {
        '$addFields': {
            'NikitaO': 'i love Mongodb'
        }
    }
])

from pymongo import MongoClient #Spotify
client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
result = client['ich']['Spotify_Youtube'].aggregate([
    {
        '$sort': {
            'Stream': -1
        }
    }, {
        '$limit': 20
    }, {
        '$addFields': {
            'NikitaO': 'i love Mongodb'
        }
    }
])

table_name = 'top20youtube_Nikita', 'top20spotify_Nikita'