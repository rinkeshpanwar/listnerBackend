from db.base import question_db
from models.question import Question as QuestionModel
from models.question import Tags as TagModel
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import status

class QuestionCrud:
    def create_question(self, question, db:Session):
        db.begin()
        try:
            title_text_tag = question["title"].split(" ")
            for tag in title_text_tag:
                question["description_text_tag"].append(tag.lower())
            # return question_db.put({**question, "answers": []})
            questions = QuestionModel()
            questions.title = question['title']
            questions.description = question['description']
            questions.created_at = question['created_at']
            questions.upvotes = question['upvotes']
            questions.downvotes = question['downvotes']
            questions.views =  question['views']
            questions.user_id =  question['user_id']
            db.add(questions)
            db.flush()
            tags = []
            for tag in question['description_text_tag']:
                tag_db = TagModel()
                tag_db.tagName = tag
                tag_db.question_id = questions.id
                tags.append(tag_db)
            db.add_all(tags)
            db.commit()
            return JSONResponse(content={"message": "Created"}, status_code=status.HTTP_201_CREATED)
        except Exception as e:
            db.rollback()
            return JSONResponse(content={"message": "there was some problem while adding data"}, status_code=status.HTTP_400_BAD_REQUEST)
    
    def get_question_by_key(self, question_key: str):
        return question_db.get(question_key)
    
    def get_question_by_username(self, question):
        pass
    
    def upvote_question(self, question_key: str):
        updates = {
            "upvotes": question_db.util.increment(1)
        }
        return question_db.update(updates, question_key)
    
    def downvote_question(self, question_key: str):
        updates = {
            "downvotes": question_db.util.increment(1)
        }
        return question_db.update(updates, question_key)

    def viewed_question(self, question_key: str):
        updates = {
            "views": question_db.util.increment(1)
        }
        return question_db.update(updates, question_key)
        
CRUDQuestion = QuestionCrud()