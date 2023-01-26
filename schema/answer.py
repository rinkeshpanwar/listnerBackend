from pydantic import BaseModel

class AnswerBase(BaseModel):
    answer: str

    class Config:
        orm_mode = True

class CreateAnswerRequest(AnswerBase):
    question_key: str

    class Config:
        orm_mode = True

class CreateAnswerInDb(AnswerBase):
    username: str
    question_key: str

    class Config:
        orm_mode = True

class CreateAnswerResponse(CreateAnswerInDb):
    key: str

    class Config:
        orm_mode = True