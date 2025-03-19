from typing import List, Any
from pymongo import MongoClient
from src.config.enum_helper import enum

class ListingsRepository:
    def __init__(self, db: MongoClient):
        self.db = db
        self.collection = db['sample_airbnb']['listingsAndReviews']
        self.model_id = enum["embedding_model_id"]
    
    def get_matching_listings(self, embedded_query: str) -> List[Any]:
        print('Performing vector search on MongoDB')
        results = self.collection.aggregate([
            {
                "$vectorSearch": {
                    "queryVector": embedded_query,
                    "path": f"embedding_{self.model_id}",
                    "numCandidates": 1000,
                    "limit": 4,
                    "index": f"embedding_{self.model_id}_index"
                }
            },{
                "$match": {
                    "amenities": {"$all": ["Wifi", "Laptop friendly workspace"]}
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "listing_url": 1,
                    "name": 1,
                    "summary": 1,
                    "price": {"$convert": {"input": "$price", "to": "double"}},
                    "address": 1,
                    "rating": 1,
                    "images":1,
                    "amenities": 1,
                }
            }
        ])
        
        return list(results)