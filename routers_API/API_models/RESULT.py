from sqlalchemy import Column, Integer, String,ForeignKey,BOOLEAN,NVARCHAR,VARCHAR,DATE
from ..database import Base
from typing import Optional
from . import USER,CADIDATES,QUESTION,SUBJECT
from  sqlalchemy.orm import relationship
from sqlalchemy import DATETIME

class result(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    cadidates_id = Column(Integer, ForeignKey("candidates.id"))
    answer_result = Column(VARCHAR(2000))
    create_at = Column(DATETIME)

    create_re_subject2 = relationship("subjects", back_populates="create_re_result")
    create_re_candidate = relationship("candidates",back_populates= "create_re_rusult")