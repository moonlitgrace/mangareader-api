from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.v1.router import router as api_v1_router

tags_metadata = [
    {
        "name": "API v1",
        "description": "Version 1 endpoints of the MangaReader API. Access manga content, search for specific titles, and retrieve manga information.",
    },
]

description = """
A Python-based web scraping tool built with FastAPI that provides easy access to manga content from the [mangareader.to](https://mangareader.to) website.
This API allows users to retrieve up-to-date information.
Enabling developers to create their own manga-related applications and services.
"""

root_router = APIRouter()

app = FastAPI(
    openapi_tags=tags_metadata,
    title="MangaReader API",
    description=description,
    summary="A Python-based web scraping API built with FastAPI that provides easy access to manga contents.",
    version="1.0.0",
    # disable redoc and swagger
    redoc_url=None,
    docs_url=None,
)

# cors
# https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
origins = [
    # specify allowed origins
    "*"  # if specified remove this lint
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://stackoverflow.com/a/61644963/20547892
app.mount(
    "/static",
    StaticFiles(directory="static"),
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
app.include_router(api_v1_router, prefix="/api/v1", tags=["API v1"])
