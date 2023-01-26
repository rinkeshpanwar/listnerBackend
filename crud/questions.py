from db.base import listner_db
from schema.questions import QuestionCreate
from utils.utlis import COLLECTION, QUESTION_COLLECTION


class QuestionCrud:
    def create_question(self, question: QuestionCreate):
        return listner_db.put({**question, COLLECTION: QUESTION_COLLECTION})
    
    def get_question_by_key(self, question_key: str):
        return listner_db.get(question_key)
    
    def get_question_by_username(self, question):
        pass
        
CRUDQuestion = QuestionCrud()