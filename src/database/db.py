from pymongo import MongoClient
from os import getenv

url = getenv("MONGO_URL", "mongodb://localhost:27017")
db_name = getenv("DB_NAME", "test_db_traduzo")

client = MongoClient(url)
db = client[db_name]
