from typing import List, Any
from src.repository.embeddings import EmbeddingsRepository
from src.repository.listings import ListingsRepository

class RecommendationService:
    def __init__(self, listings_repository: ListingsRepository, embeddings_repository: EmbeddingsRepository):
        self.listings_repository = listings_repository
        self.embeddings_repository = embeddings_repository


    def recommend(self, query: str) -> List[Any]:
        embedded_query = self.embeddings_repository.get_embeddings(query)
        recommendations = self.listings_repository.get_matching_listings(embedded_query)

        return recommendations