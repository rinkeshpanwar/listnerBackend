from pydantic import BaseModel
from typing import Any, List

class SearchBase(BaseModel):
    search: str

    class Config:
        orm_mode = True
        