from typing import List, Optional,Dict
from pydantic import BaseModel,Json,ValidationError,validator
from datetime import date,datetime
from passlib.context import CryptContext
from .subject_sche import subjects


class results(BaseModel):
    answer_result : str
    create_at: Optional[date] = None
    create_re_subject2 : subjects
    class Config():
        orm_mode = True


class Show_result(BaseModel):
    answer_result: str
    class Config():
        orm_mode = True