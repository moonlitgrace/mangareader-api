from fastapi import APIRouter, Request
from server.decorators import return_on_404
from .parsers import MangaParser, SearchParser
from server.functions.url import get_url
from server.models import Search, Manga
from typing import List

router = APIRouter()


@router.get("/manga/{query}", response_model=Manga)
@return_on_404()
async def manga(query: str):
    manga_parser = MangaParser(query)
    return manga_parser.build_dict()


@router.get("/search/{query}", response_model=List[Search])
@return_on_404()
async def search(query: str, request: Request):
    search_parser = SearchParser(query, api_url=get_url(request))
    return search_parser.build_list()
