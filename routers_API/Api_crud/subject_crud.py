from fastapi import APIRouter
from .. import oauth2
from ..API_models import SUBJECT
from ..database import get_db
from typing import List
from  ..Api_schemas import subject_sche,login_sche
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response




def create_suject_crud(request : subject_sche.subjects, db:Session = Depends(get_db)):
    new_subject = SUBJECT.subjects(title = request.title, create_at = request.create_at)
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return "Create successful"


def getall_subject_crud(db: Session = Depends(get_db)):
    get_all_sub = db.query(SUBJECT.subjects).all()
    if not get_all_sub:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get")
    return get_all_sub


def update_subject_crud(id:int, request: subject_sche.Show_subject , db:Session= Depends(get_db)):
    update_sub=db.query(SUBJECT.subjects).filter(SUBJECT.subjects.id == id)
    if not update_sub.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    update_sub.update({'id':id,'title':request.title})
    db.commit()
    return "successful"


def delete_subject_crud(id:int, db: Session = Depends(get_db)):
    delete_sub = db.query(SUBJECT.subjects).filter(SUBJECT.subjects.id == id).delete(synchronize_session=False)
    if not delete_sub:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "successful"