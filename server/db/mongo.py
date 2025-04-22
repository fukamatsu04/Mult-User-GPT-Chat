from pymongo import MongoClient
from flask import current_app, g

def init_db():
    uri = current_app.config["MONGO_URI"]
    client = MongoClient(uri)
    g.mongo_client = client

def get_db():
    if 'mongo_client' not in g:
        init_db()
    db_name = current_app.config.get("MONGO_DBNAME")
    if db_name:
        return g.mongo_client[db_name]
    return g.mongo_client.get_default_database()

def close_db(e=None):
    client = g.pop('mongo_client', None)
    if client is not None:
        client.close()