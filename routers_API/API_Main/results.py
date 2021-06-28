from fastapi import APIRouter
from .. import oauth2
from ..API_models import RESULT
from ..database import get_db
from typing import List
from ..Api_schemas import result_sche,login_sche
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
from ..Api_crud import result_crud
router = APIRouter(
    prefix="/results",
    tags=['result']

)




@router.post("/create",status_code=status.HTTP_201_CREATED)
def create_result(id, request : result_sche.results, db :Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return result_crud.create_result_crud(id,request,db)

@router.get("/getall",status_code=status.HTTP_200_OK,response_model=List[result_sche.results])
def getall_result(respone : Response, db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return result_crud.getall_result_crud(db)

@router.put("/update/{id}",status_code= status.HTTP_202_ACCEPTED)
def update_result(id : int, respone : Response, requests: result_sche.results,subject_id : int = None, db:Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return result_crud.update_result_crud(id,requests,subject_id,db)

@router.delete("/delete/{id}",status_code=status.HTTP_202_ACCEPTED)
def delete_result(id : int, db:Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return result_crud.delete_result_crud(id,db)
