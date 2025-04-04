from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv(override=True)

_db_client = None

def get_db_client() -> MongoClient:
    global _db_client
    if _db_client is None:
        print('starting Mongo instance')
        mongo_uri = os.getenv("MONGODB_URI")
        _db_client = MongoClient(mongo_uri)
    return _db_client