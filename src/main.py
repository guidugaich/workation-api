from fastapi import FastAPI
import uvicorn

from src.router.recommendation import recommendation_router

app: FastAPI = FastAPI()

@app.get("/")
def healthcheck() -> dict[str, str]:
    return {"status": "healthy"}

app.include_router(recommendation_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)