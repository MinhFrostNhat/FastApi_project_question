from fastapi import APIRouter
from .. import oauth2
from ..API_models import QUESTION
from ..database import get_db
from ..Api_schemas import question_sche,login_sche
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
from ..Api_crud import questions_crud
router = APIRouter(
    prefix="/question",
    tags=['questions']
)



@router.post("/create",status_code=status.HTTP_201_CREATED)
def create_question(id:int, request : question_sche.questions, db :Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return questions_crud.create_question_crud(request,db)


@router.get("/getall",status_code=status.HTTP_200_OK,response_model=List[question_sche.questions])
def getall_question( db: Session = Depends(get_db),get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return questions_crud.getall_question_crud(db)

@router.get("/get_spec/{id}",status_code=status.HTTP_200_OK,response_model=question_sche.questions)
def get_question(id: int ,db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return questions_crud.get_question_crud(id,db)


@router.put("/update",status_code=status.HTTP_202_ACCEPTED)
def update_question(id:int, response: Response, request: question_sche.questions,subject_id : int =None, db:Session =Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return questions_crud.update_question_crud(id,request,subject_id,db)
@router.delete("/delete/{id}",status_code= status.HTTP_202_ACCEPTED)
def delete_question(id:int, response: Response, db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return questions_crud.delete_question_crud(id,db)
