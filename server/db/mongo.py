from pymongo import MongoClient
from config import Config

def init_db():
    client = MongoClient(Config.MONGO_URI)
    db = client.get_database()
    messages_collection = db.messages
