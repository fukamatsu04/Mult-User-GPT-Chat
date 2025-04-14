from pymongo import MongoClient
from flask import current_app

def init_db():
    uri = current_app.config["MONGO_URI"]
    client = MongoClient(uri)
    current_app.mongo = client.get_default_database()
