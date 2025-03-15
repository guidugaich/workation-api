from pydantic import BaseModel
from typing import List

# Request schema
class RecommendationRequest(BaseModel):
    query: str

# Response schema
class ListingResponse(BaseModel):
    name: str
    city: str
    price: float
    description: str
    amenities: List[str]

class RecommendationResponse(BaseModel):
    recommendations: List[ListingResponse]
    note: str