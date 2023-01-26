from fastapi import APIRouter, Depends
from schema.questions import QuestionCreateResponse, QuestionBase, UpdateQuestionRequest
from api.auth import get_current_user
from crud.questions import CRUDQuestion
router = APIRouter()

@router.post("/", response_model=QuestionCreateResponse)
def create_question(question: QuestionBase, user = Depends(get_current_user)):
    return CRUDQuestion.create_question(question={**question.dict(), "username": user.username})

@router.delete("/{question_key}")
def delete_question(question_key: UpdateQuestionRequest, user = Depends(get_current_user)):
    # check if question exists and is owned by user
    pass

