from pydantic import BaseModel, Field

class QuestionBase(BaseModel):
    title: str = Field(min_length=5)
    description: str = Field(min_length=10)
    description_text_tag: list = None
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
