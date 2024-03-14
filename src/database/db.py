from pymongo import MongoClient
from os import environ

url = environ.get("MONGO_URL", "mongodb://localhost:27017")
db_name = environ.get("DB_NAME", "test_db_traduzo")

client = MongoClient(url)
db = client[db_name]
