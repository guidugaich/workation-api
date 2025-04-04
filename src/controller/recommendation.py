from typing import List, Any
from src.service.recommendation import RecommendationService

class RecommendationController:
    def __init__(self, recommendation_service: RecommendationService):
        self.recommendation_service = recommendation_service

    def recommend(self, query: str) -> List[Any]:
        response = self.recommendation_service.recommend(query)
        
        return response