from typing import List, Optional,Dict
from pydantic import BaseModel,Json,ValidationError,validator
from datetime import date,datetime
from passlib.context import CryptContext


l=['1','2','3','4','5','6','7','8','9','0']
d1=datetime(1965,12,31)
class cadidates(BaseModel):
    name : str
    email : str
    DoB : date
    position : str
    create_at: date
    class Config():
        orm_mode = True

class input_candidates(BaseModel):
    name: str
    email: str
    DoB: date
    position: str
    @validator('name')
    def abc(cls,b):
        if not b:
            raise ValueError('name can not be blank')
        for x in l:
            if x in b:
                raise ValueError(f'name is not content number')
        return b
    @validator('email')
    def not_email(cls,email):
        if '@' not in email:
            raise ValueError(f'email must have @')
        if not email:
            raise ValueError(f'email can not be blank')
        return email
    @validator('DoB')
    def not_DoB(cls,DoB):
        if not DoB:
            raise ValueError(f'Dob can not be blank')
        return DoB


    class Config():
        orm_mode = True