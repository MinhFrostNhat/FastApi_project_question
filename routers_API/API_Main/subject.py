from fastapi import APIRouter
from .. import oauth2
from ..API_models import SUBJECT
from ..database import get_db
from typing import List
from  ..Api_schemas import subject_sche,login_sche
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
from ..Api_crud import subject_crud
router = APIRouter(
    tags=['subject'],
    prefix="/subject"
)


@router.post("/create",status_code=status.HTTP_202_ACCEPTED)
def create_suject(request : subject_sche.subjects, db:Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return subject_crud.create_suject_crud(request,db)

@router.get("/getall",status_code=status.HTTP_200_OK)
def getall_subject(db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return subject_crud.getall_subject_crud(db)


@router.put("/update/{id}",status_code= status.HTTP_202_ACCEPTED,tags=['subject'])
def update_subject(id:int, request: subject_sche.Show_subject , db:Session= Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return subject_crud.update_subject_crud(id,request,db)


@router.delete("/delete/{id}",status_code= status.HTTP_202_ACCEPTED)
def delete_subject(id:int,db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return subject_crud.delete_subject_crud(id,db)