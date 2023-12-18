from fastapi import APIRouter

from .parsers import MangaParser, SearchParser
from ...decorators import return_on_404

router = APIRouter()


@router.get("/manga/{query}")
@return_on_404()
async def manga(query: str):
    manga_parser = MangaParser(query)
    return manga_parser.build_dict()


@router.get("/search/{query}")
@return_on_404()
async def search(query: str):
    search_parser = SearchParser(query)
    return search_parser.build_list()
