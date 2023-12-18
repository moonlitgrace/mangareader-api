from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# https://fastapi.tiangolo.com/advanced/templates/
templates = Jinja2Templates(directory="client/templates/")


# homepage route
@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
        },
    )
