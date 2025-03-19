from fastapi import Depends

from src.config.cache import get_cache_client
from src.config.database import get_db_client
from src.config.client import get_openai_client
from src.repository.embeddings import EmbeddingsRepository
from src.repository.listings import ListingsRepository
from src.service.recommendation import RecommendationService

def get_listings_repository() -> ListingsRepository:
    return ListingsRepository(get_db_client())

def get_embeddings_repository() -> EmbeddingsRepository:
    return EmbeddingsRepository(get_openai_client(), get_cache_client())

def get_recommendation_service(
    listings_repository: ListingsRepository = Depends(get_listings_repository),
    embeddings_repository: EmbeddingsRepository = Depends(get_embeddings_repository),
) -> RecommendationService:
    return RecommendationService(listings_repository, embeddings_repository)