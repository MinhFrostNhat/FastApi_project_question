from fastapi import APIRouter
from .. import oauth2
from ..API_models import USER
from ..database import get_db
from ..Api_schemas import user_sche,login_sche
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
from .. import hashing

def get_user_by_username(db: Session, username: str):
    return db.query(USER.userinfo).filter(USER.userinfo.username == username).first()


def create_user(db: Session, user: user_sche.UserCreate):
    db_user = USER.userinfo(username=user.username, fullname=user.fullname,password=hashing.Hash.bycrypt(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "successfull"


def get_all_user(db: Session = Depends(get_db)):
    get_all=db.query(USER.userinfo).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not have data to get")
    return get_all


def list_spec_user_crud(id:int, db: Session = Depends(get_db)):
    get_spec_user = db.query(USER.userinfo).filter(USER.userinfo.id == id).first()
    if not get_spec_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    return get_spec_user

def update_user_crud(id, requests: user_sche.UserCreate, db: Session = Depends(get_db)):
    update_user_info=db.query(USER.userinfo).filter(USER.userinfo.id == id)
    if not update_user_info.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    update_user_info.update({"id":id,"fullname":requests.fullname,"password":requests.password})
    db.commit()
    return "good update successful"

def delete_crud(id, db: Session = Depends(get_db)):
    delete_user_info = db.query(USER.userinfo).filter(USER.userinfo.id == id).delete(synchronize_session=False)
    if not delete_user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found this {id}")
    db.commit()
    return "delete successful"