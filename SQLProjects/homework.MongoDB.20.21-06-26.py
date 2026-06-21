#task1
import re
from pymongo import MongoClient
filter={
    'borough': 'Staten Island',
    'name': re.compile(r"pizza(?i)")
}

result = client['sample_data']['restaurants'].find(
  filter=filter
)

#task2

from pymongo import MongoClient
result = client['sample_data']['restaurants'].aggregate([
    {
        '$addFields': {
            'averageScore': {
                '$avg': '$grades.score'
            }
        }
    }, {
        '$sort': {
            'averageScore': -1
        }
    }, {
        '$limit': 5
    }, {
        '$project': {
            'name': 1
        }
    }
])