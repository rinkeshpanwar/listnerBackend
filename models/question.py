from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Relationship
from db.base import Base

class Question(Base):
    id = Column(Integer, autoincrement= True, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    upvotes = Column(Integer, nullable=False)
    downvotes = Column(Integer, nullable=False)
    views = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    comment = Relationship('Comment', back_populates='question')
    user = Relationship('User', back_populates='question')
    tags = Relationship('Tags', back_populates='question')
    answer = Relationship('Answer', back_populates='question')

class Comment(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    comment = Column(Text, nullable= False)

    question_id = Column(Integer, ForeignKey('question.id'))
    question = Relationship('Question', back_populates='comment')

class Tags(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    tagName = Column(String(200), nullable= False, index=True)
    question_id = Column(Integer, ForeignKey('question.id'))

    question = Relationship('Question', back_populates='tags')
