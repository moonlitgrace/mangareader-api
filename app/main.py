from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

from api.api_v1.router import router as api_v1_router

tags_metadata = [
    {
        "name": "Version 1",
        "description": "Endpoints related to version 1 of the MangaReader API. Access manga content, search for specific titles, and retrieve manga information.",
    },
]

root_router = APIRouter()
app = FastAPI(
    openapi_tags=tags_metadata,
    title="MangaReader API",
    description="""
            A Python-based web scraping tool built with FastAPI that provides easy access to manga content from the [mangareader.to](https://mangareader.to) website.
            This API allows users to retrieve up-to-date information.
            Enabling developers to create their own manga-related applications and services.
        """,
    summary="A Python-based web scraping API built with FastAPI that provides easy access to manga contents.",
    version="0.2.0",
)

# https://stackoverflow.com/a/61644963/20547892
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

# https://fastapi.tiangolo.com/advanced/templates/
TEMPLATES = Jinja2Templates(directory="templates")


# homepage route
@root_router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root(request: Request):
    return TEMPLATES.TemplateResponse(
        "index.html",
        context={
            "request": request,
        },
    )


app.include_router(root_router)
app.include_router(api_v1_router, prefix="/api/v1", tags=["Version 1"])
