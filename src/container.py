from fastapi import Depends

from src.config.database import get_db_client
from src.repository.listings import ListingsRepository
from src.service.recommendation import RecommendationService

def get_listings_repository() -> ListingsRepository:
    return ListingsRepository(get_db_client())

def get_recommendation_service(listing_repo: ListingsRepository = Depends(get_listings_repository)) -> RecommendationService:
    return RecommendationService(listing_repo)