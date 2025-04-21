from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()
messages_collection = db.messages  # Define as a global variable

def init_db():
    # Initialize the database (if needed for other setup tasks)
    pass
