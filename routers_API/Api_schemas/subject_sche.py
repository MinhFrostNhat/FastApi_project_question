from typing import List, Optional,Dict
from pydantic import BaseModel,Json,ValidationError,validator
from datetime import date,datetime
from passlib.context import CryptContext








class subjects(BaseModel):
    title : str
    create_at : date

    @validator('title')
    def title_no_(cls, u):
        if not u:
            raise ValueError(f'title can not blank')
        return u
    class Config():
        orm_mode = True


class Show_subject(BaseModel):
    title : str
    class Config():
        orm_mode = True


