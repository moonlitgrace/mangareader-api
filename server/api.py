from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from .routes import router

app = FastAPI()
app.include_router(router, prefix="/api")


# overrite "openapi.json"
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MangaAPI",
        summary="A Python-based web scraping API built with FastAPI that provides easy access to manga contents.",
        version="0.1.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
