from fastapi import APIRouter, Depends, status, HTTPException
from schema.answer import CreateAnswerRequest, CreateAnswerResponse
from api.auth import get_current_user
from crud.answer import CRUDAnswer
from crud.questions import CRUDQuestion
router = APIRouter()

@router.post("/", response_model=CreateAnswerResponse, status_code=status.HTTP_201_CREATED)
def create_answer(answer: CreateAnswerRequest, user = Depends(get_current_user)):
    return CRUDAnswer.create_answer(answer={**answer.dict(), "id": user.id})

@router.get("/{question_id}")
def get_answers(question_id: str):
    return CRUDAnswer.get_answers(question_id=question_id)

@router.delete("/{answer_id}")
def delete_answer(answer_id: str, user = Depends(get_current_user)):
    return CRUDAnswer.delete_answer(answer_id=answer_id, user=user)