from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session
from combat_manager.responses.user import UserResponse
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