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
    user_id: int
    question_key: str

    class Config:
        orm_mode = True

class CreateAnswerResponse(CreateAnswerInDb):
    id: int

    class Config:
        orm_mode = True