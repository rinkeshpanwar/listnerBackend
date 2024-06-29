from fastapi import APIRouter, Depends
from api.auth import get_current_user
from schema.search import SearchBase
from crud.search import CRUDSearch

router = APIRouter()

@router.post("/")
def get_search_question(search: SearchBase, user = Depends(get_current_user)):
    return CRUDSearch.search_question(search)

