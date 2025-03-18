from typing import List, Any
from pymongo import MongoClient
from scripts.embed_database_one_off import embedding_model_id

class ListingsRepository:
    def __init__(self, db: MongoClient):
        self.db = db
        self.collection = self.db['sample_airbnb']['listingsAndReviews']
    
    def get_matching_listings(self, embedded_query: str) -> List[Any]:
        results = self.collection.aggregate([
            {
                "$vectorSearch": {
                    "queryVector": embedded_query,
                    "path": "plot_embedding",
                    "numCandidates": 1000,
                    "limit": 10,
                    "index": f"embedding_{embedding_model_id}_index"
                }
            }
        ])
        
        return results