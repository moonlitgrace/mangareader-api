from fastapi import APIRouter

from .parsers import MangaParser

router = APIRouter()

@router.get("/manga/{query}")
async def test(query: str):
    manga_parser = MangaParser(query)
    return manga_parser.build_dict()
