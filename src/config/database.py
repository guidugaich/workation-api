from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

_db_client = None

def get_db_client() -> MongoClient:
    global _db_client
    if _db_client is None:
        mongo_uri = os.getenv("MONGO_URI")
        _db_client = MongoClient(mongo_uri)
    return _db_client