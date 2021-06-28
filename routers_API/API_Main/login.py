from fastapi import APIRouter
from .. import oauth2,jwttoken

from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from  ..API_models import USER
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,HTTPException,status,Response
router = APIRouter()




@router.post("/login",status_code=status.HTTP_200_OK,tags=['login'])
def login_sys(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    userr = db.query(USER.userinfo).filter(USER.userinfo.username == request.username).first()
    if not userr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect username")
    if not Hash.verify(userr.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password")

    access_token = jwttoken.create_access_token(data={"sub": userr.username})
    return {"access_token": access_token, "token_type": "bearer"}