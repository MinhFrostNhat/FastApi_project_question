from sqlalchemy import Column, Integer, String,ForeignKey,BOOLEAN,NVARCHAR,VARCHAR,DATE
from ..database import Base
from typing import Optional
from . import USER,SUBJECT,QUESTION
from  sqlalchemy.orm import relationship
from sqlalchemy import DATETIME


class candidates(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(225))
    email = Column(VARCHAR(225))
    DoB = Column(DATE)
    position = Column(VARCHAR(225))
    create_at = Column(DATETIME)

    create_re_rusult = relationship("result", back_populates="create_re_candidate")