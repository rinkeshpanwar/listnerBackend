from db.base import answer_db, question_db
from schema.answer import CreateAnswerInDb


class AnswerCrud:
    def create_answer(self, answer: CreateAnswerInDb):
        answer_in_db = answer_db.put({**answer})
        updates = {
            "answers": question_db.util.append(answer_in_db["key"])
        }
        question_db.update(updates,answer["question_key"])
        return answer_in_db
    
    def get_answers(self, question_id: str):
        question = question_db.get(question_id)
        answers = [answer_db.get(answer_id) for answer_id in question["answers"]]
        return answers
    

CRUDAnswer = AnswerCrud()