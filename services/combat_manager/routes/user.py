from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from combat_manager.responses.user import UserResponse, LoginResponse
from combat_manager.schemas.user import RegisterUserRequest
from combat_manager.database import get_db
from combat_manager.models.user import User
from combat_manager.utils import user


user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@user_router.post("",
                 status_code=status.HTTP_201_CREATED,response_model=UserResponse)
async def register_user(data: RegisterUserRequest,session: Session
                        =Depends(get_db)):
    return await user.create_user_account(data, session) 

@user_router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
async def user_login(data:OAuth2PasswordRequestForm =  Depends(), session: Session=Depends(get_db)):
    return await user.get_login_token(data,  session)