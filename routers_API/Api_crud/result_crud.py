from fastapi import APIRouter
from .. import oauth2
from ..API_models import RESULT
from ..database import get_db
from typing import List
from ..Api_schemas import result_sche,login_sche
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response


def create_result_crud(id:int, request : result_sche.results, db :Session = Depends(get_db)):
    new_result= RESULT.result(answer_result = request.answer_result, create_at = request.create_at, subject_id = id)
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return "Create successful"

def getall_result_crud(db: Session = Depends(get_db)):
    getall_res = db.query(RESULT.result).all()
    if not getall_res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found")
    return getall_res


def update_result_crud(id : int, requests: result_sche.results,subject_id : int = None, db:Session = Depends(get_db)):
    update_res = db.query(RESULT.result).filter(RESULT.result.id == id)
    if not update_res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    update_res.update({'id':id,'answer_result': requests.answer_result,'subject_id': subject_id})
    db.commit()
    return "successful"


def delete_result_crud(id : int, db:Session = Depends(get_db)):
    delete_res = db.query(RESULT.result).filter(RESULT.result.id == id).delete(synchronize_session=False)
    if not delete_res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "delete successful"