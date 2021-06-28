from sqlalchemy import Column, Integer, String,ForeignKey,BOOLEAN,NVARCHAR,VARCHAR,DATE
from ..database import Base
from typing import Optional
from . import USER,CADIDATES,QUESTION
from  sqlalchemy.orm import relationship
from sqlalchemy import DATETIME


class subjects(Base):

    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(225))
    create_re_question = relationship("questions", back_populates="create_re_subject")
    create_re_result = relationship("result",back_populates="create_re_subject2")

    create_at = Column(DATETIME)