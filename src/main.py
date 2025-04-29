from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.router.recommendation import recommendation_router

app: FastAPI = FastAPI()

@app.get("/")
def healthcheck() -> dict[str, str]:
    return {"status": "healthy"}

app.include_router(recommendation_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)