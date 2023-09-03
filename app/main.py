from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
# v1 api
from app.api.v1.endpoints import router as v1_router

app = FastAPI()

# v1 api routes
app.include_router(v1_router, prefix="/v1")

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