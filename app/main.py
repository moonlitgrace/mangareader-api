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
description = """
### Description

[**MangaAPI**](https://github.com/tokitou-san/MangaAPI) is a Python-based web scraping tool built with FastAPI that provides easy access to manga content 
from the mangareader.to website. This API allows users to retrieve up-to-date information about various manga 
titles, chapters, and pages, enabling developers to create their own manga-related applications and services.
"""

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MangaAPI",
        version="0.1.0",
        summary="A Python-based web scraping API built with FastAPI that provides easy access to manga contents.",
        description=description,
        servers=[
            {
                "url": "https://manga-api-70c3.onrender.com/v1",
                "description": "v1 API"
            }
        ],
        license_info={
            "name": "MIT",
            "identifier": "MIT",
            "url": "https://github.com/tokitou-san/MangaAPI/blob/main/LICENSE"
        },
        terms_of_service="https://github.com/tokitou-san/MangaAPI/blob/main/LICENSE",
        contact={
            "name": "Tokito",
            "url": "https://github.com/tokitou-san",
        },
        routes=app.routes,
        openapi_version="3.1.0",
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi