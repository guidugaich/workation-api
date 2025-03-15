from typing import List, Any
from pymongo import MongoClient

class ListingsRepository:
    def __init__(self, db: MongoClient):
        self.db = db['sample_airbnb']['listingsAndReviews']

    def get_matching_listings(self, embedded_query: str) -> List[Any]:
        print('will call vector db', embedded_query)
        return []