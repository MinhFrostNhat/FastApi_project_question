from typing import List, Optional,Dict
from pydantic import BaseModel,Json,ValidationError,validator
from datetime import date,datetime
from passlib.context import CryptContext
from .subject_sche import subjects


class questions(BaseModel):
    title : str
    answer_a : str
    answer_b : str
    type : int
    create_at : Optional[date] = None
    create_re_subject: subjects

    @validator('title','answer_a','answer_b')
    def title_no_(cls, u):
        if not u:
            raise ValueError(f'title and answers can not blank')
        return u

    class Config():
        orm_mode = True

class Show_questions(BaseModel):
    id : int
    title: str
    answer_a: str
    answer_b: str
    class Config():
        orm_mode = True