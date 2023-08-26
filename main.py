from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
	return { "message": "MangaAPI" }

@app.get("/v1")
async def v1_api() -> dict[str, str]:
	return { "message": "MangaAPI V1 API" }