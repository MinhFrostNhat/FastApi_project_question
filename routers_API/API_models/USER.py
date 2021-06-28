from sqlalchemy import Column, Integer, String,ForeignKey,BOOLEAN,NVARCHAR,VARCHAR,DATE
from ..database import Base
from typing import Optional
from  sqlalchemy.orm import relationship
from sqlalchemy import DATETIME
class userinfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(225), unique=True)
    password = Column(String(255))
    fullname = Column(String(225), unique=True)