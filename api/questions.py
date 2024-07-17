from fastapi import APIRouter, Depends
from schema.questions import QuestionCreateResponse, QuestionBase, UpdateQuestionRequest
from api.auth import get_current_user
from datetime import datetime
from crud.questions import CRUDQuestion
from deps import get_db
router = APIRouter()

@router.post("/")
def create_question(question: QuestionBase, user = Depends(get_current_user), db = Depends(get_db)):
    return CRUDQuestion.create_question(question={**question.dict(), "username": user.username, "created_at": str(datetime.now()), "updated_at": str(datetime.now()), "upvotes": 0, "downvotes": 0, "views": 0, "user_id" : user.id}, db=db)

@router.get("/{question_key}")
def get_question(question_key: str, user = Depends(get_current_user)):
    return CRUDQuestion.get_question_by_key(question_key)

@router.put("/upvote/{question_key}")
def upvote_question(question_key: str, user = Depends(get_current_user)):
    return CRUDQuestion.upvote_question(question_key)

@router.put("/downvote/{question_key}")
def downvote_question(question_key: str, user = Depends(get_current_user)):
    return CRUDQuestion.downvote_question(question_key)

@router.put("/views/{question_key}")
def viewed_question(question_key: str, user = Depends(get_current_user)):
    return CRUDQuestion.viewed_question(question_key)

# @router.delete("/{question_key}")
# def delete_question(question_key: UpdateQuestionRequest, user = Depends(get_current_user)):
#     # check if question exists and is owned by user
#     pass

