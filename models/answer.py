from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Relationship
from datetime import datetime
from db.base import Base

class Answer(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    answer = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"), nullable=False)
    answer_by = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    question = Relationship('Question', back_populates='answer')
    user = Relationship('User', back_populates='answer')
