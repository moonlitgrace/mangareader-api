from fastapi import APIRouter
from .parser import MangaReader

router = APIRouter()


@router.get("/manga/{query}")
async def manga(query: str):
    manga_reader = MangaReader()
    return manga_reader.get_manga(query=query)
