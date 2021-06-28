from fastapi import APIRouter
from .. import oauth2
from ..database import get_db
from ..API_models import CADIDATES,QUESTION,RESULT,USER
from ..Api_schemas import result_sche,question_sche,cadidates_sche,login_sche
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response,File,UploadFile
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError


def create_cadidates_crud(request: cadidates_sche.input_candidates,db:Session = Depends(get_db)):
    try:
        new_cadidates= CADIDATES.candidates(name = request.name, email = request.email, DoB = request.DoB, position = request.position)
        db.add(new_cadidates)
        db.commit()
        db.refresh(new_cadidates)
        return "Create successful"
    except ValidationError as e:
        return e


def get_question_crud(db: Session = Depends(get_db)):
    getall_question = db.query(QUESTION.questions).all()
    if not getall_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to display")
    return getall_question

def get_question_crud_i(id:int,db: Session = Depends(get_db)):
    getall_question = db.query(QUESTION.questions).filter(QUESTION.questions.id==id).first()
    if not getall_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    return getall_question

def get_result_crud(id:int,db: Session = Depends(get_db)):
    get_user_result = db.query(RESULT.result).filter(RESULT.result.id == id).first()
    if not get_user_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    return get_user_result

def getall_candidates_crud(db: Session = Depends(get_db)):
    get_candidates = db.query(CADIDATES.candidates).all()
    if not get_candidates:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get")
    return get_candidates

def get_cadidates_id_crud(id: int , db: Session = Depends(get_db)):
    get_cadidates_id = db.query(CADIDATES.candidates).filter(CADIDATES.candidates.id == id).first()
    if not get_cadidates_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    return get_cadidates_id

def delete_cadidate(id: int,db: Session = Depends(get_db)):
    delete_cadidates_id = db.query(CADIDATES.candidates).filter(CADIDATES.candidates.id == id).delete(synchronize_session=False)
    if not delete_cadidates_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "delete successful"