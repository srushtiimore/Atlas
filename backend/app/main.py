from fastapi import FastAPI
from app.routers.projects import router
app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"welcome to Atlas"}

@app.get("/health")
def health():
    return {"status":"healthy"}