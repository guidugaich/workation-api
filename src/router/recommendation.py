from fastapi import APIRouter, Depends
from src.controller.recommendation import RecommendationController
from src.config.schemas.listings import RecommendationRequest, RecommendationResponse
from src.container import get_recommendation_controller

recommendation_router = APIRouter()

@recommendation_router.post("/recommend", response_model=None)
def recommend(
    request: RecommendationRequest,
    controller: RecommendationController = Depends(get_recommendation_controller),
) -> RecommendationResponse:
    response = controller.recommend(request.query)
    return response
