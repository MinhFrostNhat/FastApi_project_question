from sqlalchemy import Column, Integer, String,ForeignKey,BOOLEAN,NVARCHAR,VARCHAR,DATE
from ..database import Base
from typing import Optional
from . import USER,RESULT,SUBJECT
from  sqlalchemy.orm import relationship
from sqlalchemy import DATETIME


class questions(Base):

    __tablename__="questions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(VARCHAR(225))
    answer_a = Column(VARCHAR(225))
    answer_b = Column(VARCHAR(225))
    type = Column(Integer)
    subject_id = Column(Integer,ForeignKey("subjects.id"))
    create_at = Column(DATETIME)

    create_re_subject = relationship("subjects",back_populates = "create_re_question")