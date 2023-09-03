from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
# v1 api
from app.api.v1 import endpoints

app = FastAPI()

@app.get("/", response_class=FileResponse, include_in_schema=False)
async def root():
	return FileResponse("docs/index.html", status_code=200)

# v1 api routes
app.include_router(endpoints.router, prefix="/v1")

# overrite "openapi.json"
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MangaAPI",
        summary="A Python-based web scraping API built with FastAPI that provides easy access to manga contents.",
        version="0.1.0",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi