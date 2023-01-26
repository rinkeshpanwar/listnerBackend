from fastapi import APIRouter, Depends, status, HTTPException
from schema.answer import CreateAnswerRequest, CreateAnswerResponse
from api.auth import get_current_user
from crud.answer import CRUDAnswer
from crud.questions import CRUDQuestion
router = APIRouter()

@router.post("/", response_model=CreateAnswerResponse, status_code=status.HTTP_201_CREATED)
def create_answer(answer: CreateAnswerRequest, user = Depends(get_current_user)):
    # check if question exists
    question = CRUDQuestion.get_question_by_key(answer.question_key)
    if question is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    
    # create answer
    return CRUDAnswer.create_answer(answer={**answer.dict(), "username": user.username})