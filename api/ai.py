from fastapi import APIRouter

router = APIRouter()

@router.get("/split")
def split(text: str):
    return {"split": "tested"}

