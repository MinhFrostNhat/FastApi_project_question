from typing import List, Optional,Dict
from pydantic import BaseModel,Json,ValidationError,validator
from datetime import date,datetime
from passlib.context import CryptContext
from fastapi import Cookie

l=['1','2','3','4','5','6','7','8','9','0']

class UserInfoBase(BaseModel):
    username: str
    fullname: str

    class Config():
        orm_mode = True


class UserCreate(UserInfoBase):
    password: str

    @validator('username', 'password')
    def user_no_(cls, u):
        if not u:
            raise ValueError(f'username or password can not blank')
        return u

    @validator('fullname')
    def user_no(cls, v):
        if not v:
            raise ValueError(f'fullname can not blank')
        for x in l:
            if x in v:
                raise ValueError(f'fullname not content number')
        return v
    class Config():
        orm_mode = True


class Show_user(BaseModel):
    username: str
    fullname: str
    class Config():
        orm_mode = True