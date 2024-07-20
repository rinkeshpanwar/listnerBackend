from db.base import answer_db, question_db
from schema.answer import CreateAnswerInDb
from models.answer import Answer as AnswerModel
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import status
from datetime import datetime
class AnswerCrud:
    def create_answer(self, answer: CreateAnswerInDb,db:Session):
        # answer_in_db = answer_db.put({**answer})
        # updates = {
        #     "answers": question_db.util.append(answer_in_db["key"])
        # }
        # question_db.update(updates,answer["question_key"])
        # return answer_in_db
        answer_db = AnswerModel()
        answer_db.answer = answer['answer']
        answer_db.answer_by = answer['user_id']
        answer_db.question_id = answer['question_key']
        answer_db.created_at = datetime.now()
        db.add(answer_db)    
        db.flush()
        db.commit()
        return JSONResponse(content=True, status_code=status.HTTP_201_CREATED)

    def get_answers(self, question_id: str):
        question = question_db.get(question_id)
        answers = [answer_db.get(answer_id) for answer_id in question["answers"]]
        return answers
    

CRUDAnswer = AnswerCrud()