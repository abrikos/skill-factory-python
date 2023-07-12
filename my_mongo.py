from bson.json_util import dumps
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# Connect to our database
db = client.laboratory


def get_record(table, query):
    series_collection = db[table]
    return dumps(series_collection.find_one(query))

