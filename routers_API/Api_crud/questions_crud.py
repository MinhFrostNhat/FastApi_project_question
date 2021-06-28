from fastapi import APIRouter
from .. import oauth2
from ..API_models import QUESTION
from ..database import get_db
from ..Api_schemas import question_sche,login_sche
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response




def create_question_crud(request : question_sche.questions, db :Session = Depends(get_db)):
    newquestion = QUESTION.questions(title = request.title, answer_a = request.answer_a, answer_b = request.answer_b, type = request.type, create_at = request.create_at, subject_id = id)
    db.add(newquestion)
    db.commit()
    db.refresh(newquestion)
    return "Create successful"

def getall_question_crud( db: Session = Depends(get_db)):
    getall_ques = db.query(QUESTION.questions).all()
    if not getall_ques:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get")
    return getall_ques

def get_question_crud(id: int ,db: Session = Depends(get_db)):
    get_ques = db.query(QUESTION.questions).filter(QUESTION.questions.id == id).first()
    if not get_ques:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    return get_ques

def update_question_crud(id:int, request: question_sche.questions,subject_id : int =None, db:Session =Depends(get_db)):
    update_ques = db.query(QUESTION.questions).filter(QUESTION.questions.id == id)
    if not update_ques:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    update_ques.update({'id':id,'title':request.title, 'answer_a':request.answer_a, 'answer_b':request.answer_b,'subject_id': subject_id})
    db.commit()
    return "successful"

def delete_question_crud(id:int, db: Session = Depends(get_db)):
    delete_ques = db.query(QUESTION.questions).filter(QUESTION.questions.id == id).delete(synchronize_session=False)
    if not delete_ques:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "delete successful"