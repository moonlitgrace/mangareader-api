from fastapi import APIRouter
from .manga import MangaParser
from ...decorators import return_on_404

router = APIRouter()


@router.get("/manga/{query}")
@return_on_404()
async def manga(query: str):
    manga_parser = MangaParser(query)
    return manga_parser.build_dict()
