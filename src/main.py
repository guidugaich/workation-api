from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def healthcheck():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)