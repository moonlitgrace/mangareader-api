from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.openapi.utils import get_openapi

router = APIRouter()

# https://fastapi.tiangolo.com/advanced/templates/
templates = Jinja2Templates(directory="client/templates/")

def get_app():
    from server.api import app
    return app

# homepage route
@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    openapi = get_openapi(routes=get_app().routes, title="MangaAPI", version="0.1.0")
    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
            "openapi": openapi,
        },
    )
