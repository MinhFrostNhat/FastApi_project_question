import datetime

from fastapi import APIRouter
from .. import oauth2
from ..database import get_db
from ..API_models import CADIDATES,QUESTION,RESULT,USER
from ..Api_schemas import result_sche,question_sche,cadidates_sche,login_sche
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response,Form,File,UploadFile
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError
from ..Api_crud import candidates_crud

router = APIRouter(
    tags=['cadidates'],
    prefix="/cadidates"
)



@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_cadidates(request: cadidates_sche.input_candidates, db:Session = Depends(get_db)):
    return candidates_crud.create_cadidates_crud(request,db)


@router.get("/get-questions/",status_code=status.HTTP_200_OK,response_model=List[question_sche.Show_questions])
def get_question(db: Session = Depends(get_db)):
    return candidates_crud.get_question_crud(db)

@router.get("/get-questions/{id}",status_code=status.HTTP_200_OK,response_model=question_sche.Show_questions)
def get_question(id:int,db: Session = Depends(get_db)):
    return candidates_crud.get_question_crud_i(id,db)

@router.get("/result/{id}",status_code=status.HTTP_200_OK,response_model=result_sche.Show_result)
def get_result(id:int,db: Session = Depends(get_db)):
    return candidates_crud.get_result_crud(id,db)


@router.get("/get-candidates",status_code=status.HTTP_200_OK)
def getall_candidates(response: Response, db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return candidates_crud.getall_candidates_crud(db)

@router.post("/store-candidates",status_code=status.HTTP_201_CREATED)
async def cadidates_sumbit(answer_a : bool = Form(...),answer_b : bool = Form(...),file:UploadFile= File(...)):
    return {'answer_a ':answer_a ,'answer_b ':answer_b,"File_name":file.filename }

@router.get("/get-cadidates/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=cadidates_sche.cadidates)
def get_cadidates_id(id: int ,response: Response, db: Session = Depends(get_db),get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return candidates_crud.get_cadidates_id_crud(id,db)

@router.delete("/delete/cadidates/{id}",status_code= status.HTTP_202_ACCEPTED)
def delete_cadidate(id: int,db: Session = Depends(get_db), get_current_user : login_sche.UserCreate = Depends(
    oauth2.get_current_user)):
    return candidates_crud.delete_cadidate(id,db)