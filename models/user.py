from sqlalchemy import Column, String, Integer
from db.base import Base
class User(Base):

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    user_name = Column(String(255), unique=True, index=True)
    password = Column(String(255))