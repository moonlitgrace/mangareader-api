import uvicorn

from fastapi import APIRouter, FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

from api.api_v1.router import router as api_v1_router

root_router = APIRouter()
app = FastAPI()

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
app.include_router(api_v1_router, prefix="/v1", tags=["v1"])


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


# Run server
def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
