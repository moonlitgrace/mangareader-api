import markdown
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .routes import router

app = FastAPI()
app.include_router(router, prefix="/api")

# https://stackoverflow.com/a/61644963/20547892
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

# https://fastapi.tiangolo.com/advanced/templates/
templates = Jinja2Templates(directory="client/templates/")


# homepage route
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    # open README.md file
    with open("README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
            "readme_content": markdown.markdown(readme_content),
        },
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
