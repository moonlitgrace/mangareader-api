from enum import Enum
from fastapi import FastAPI

# v1 api
from app.api.v1 import api, endpoints

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "MangaAPI"}

app.include_router(endpoints.router, prefix="/v1")