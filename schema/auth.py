from pydantic import BaseModel

class User(BaseModel):
    username: str

    class Config:
        orm_mode = True

class Createuser(User):
    password: str

    class Config:
        orm_mode = True

class LoginUser(Createuser):
    pass

class MySelf(User):
    id: int

    class Config:
        orm_mode = True

        
    