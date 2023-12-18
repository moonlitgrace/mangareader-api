from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .providers import mangareader_router, mangakomi_router
from .docs import docs_router

# docs routes
from .docs import docs_router

app = FastAPI()

app.include_router(docs_router, prefix="", tags=["Docs"])
# set route for each providers
app.include_router(mangareader_router, prefix="/mangareader", tags=["MangaReader"])
app.include_router(mangakomi_router, prefix="/mangakomi", tags=["MangaKomi"])

# https://stackoverflow.com/a/61644963/20547892
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)


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
