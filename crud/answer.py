from db.base import listner_db
from schema.answer import CreateAnswerInDb
from utils.utlis import COLLECTION, ANSWER_COLLECTION

class AnswerCrud:
    def create_answer(self, answer: CreateAnswerInDb):
        return listner_db.put({**answer, COLLECTION: ANSWER_COLLECTION})

CRUDAnswer = AnswerCrud()