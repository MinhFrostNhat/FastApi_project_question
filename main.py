
from fastapi import Depends, FastAPI,HTTPException,status,Response,Request
from routers_API.API_Main import subject,user,question,results,cadidates,login
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
app = FastAPI(
    title="This is API project v2"
)

security=HTTPBasic()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    a= JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail":PlainTextResponse(str(exc), status_code=422).body})
    )
    return (a)



origins = [
    "http://localhost:8080",
    "http://localhost",
    "http://localhost:8080/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(subject.router)
app.include_router(question.router)
app.include_router(results.router)
app.include_router(cadidates.router)
app.include_router(login.router)

