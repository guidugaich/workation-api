from typing import List, Any
from src.repository.listings import ListingsRepository

class RecommendationService:
    def __init__(self, repository: ListingsRepository):
        self.repository = repository

    def recommend(self, query: str) -> List[Any]:
        recommendations = self.repository.get_matching_listings(query)

        return recommendations