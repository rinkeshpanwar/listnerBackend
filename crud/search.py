from db.base import question_db
from schema.search import SearchBase
from sqlalchemy.orm import Session, joinedload
from models.question import Question as QuestionModel
from models.question import Tags as TagModel

class searchCrud:
    def search_question(self, search:SearchBase, db:Session):
        text_tag = search.search.split(" ")
        # build_query = []
        
        # for tag in text_tag:
        #     build_query.append({"description_text_tag?contains": tag})

        # build_query.append({"title?contains": SearchBase.search})
        # build_query.append({"description?contains": ""})
        # return question_db.fetch(build_query)
        return db.query(QuestionModel).options(joinedload(QuestionModel.tags, innerjoin=True)).filter(TagModel.tagName.in_(text_tag)).all()


CRUDSearch = searchCrud()