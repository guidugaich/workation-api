from fastapi import APIRouter, Depends
from src.service.recommendation import RecommendationService
from src.config.schemas.listings import RecommendationRequest, RecommendationResponse
from src.container import get_recommendation_service

recommendation_router = APIRouter()

@recommendation_router.post("/recommend", response_model=None)
async def recommend(
    request: RecommendationRequest,
    service: RecommendationService = Depends(get_recommendation_service),
):
    print('request.query', request.query)
    recommendations = service.recommend(request.query)
    return {
        "recommendations": recommendations,
        "note": f"Found {len(recommendations)} top matches for '{request.query}'."
    }