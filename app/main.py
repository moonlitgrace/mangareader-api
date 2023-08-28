from fastapi import FastAPI
# v1 api
from app.api.v1 import endpoints

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "MangaAPI"}
	
# v1 api routes
app.include_router(endpoints.router, prefix="/v1")