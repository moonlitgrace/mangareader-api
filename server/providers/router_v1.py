from fastapi import APIRouter

router = APIRouter()

@router.get("/trending")
async def trending():
    return "Working..."