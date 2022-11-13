import pymongo
from pymongo import MongoClient

connection = pymongo.MongoClient(
    "mongodb+srv://waterdip:O4in8rAiySFxfDUC@cluster0.b4jlo.mongodb.net/?retryWrites=true&w=majority")

db = connection.test
