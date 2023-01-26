from pydantic import BaseModel

class QuestionBase(BaseModel):
    title: str
    description: str = None

    class Config:
        orm_mode = True

class QuestionCreateResponse(QuestionBase):
    key: str
    username: str

    class Config:
        orm_mode = True

class QuestionCreate(QuestionBase):
    username: str

    class Config:
        orm_mode = True

class UpdateQuestionRequest(QuestionBase):
    key: str

    class Config:
        orm_mode = True