from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Relationship
from db.base import Base
class User(Base):

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    user_name = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    question = Relationship('Question', back_populates='user')