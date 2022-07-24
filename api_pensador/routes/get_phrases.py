from fastapi import APIRouter
from api_pensador.services import phrases

router = APIRouter()

@router.get("/")
async def return_phrases(term: str, max: int = 0):
    return phrases.get_phrases(term, max)
