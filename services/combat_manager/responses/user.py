from typing  import Union
from datetime import  datetime

from pydantic import EmailStr
from combat_manager.responses.base import BaseResponse


class UserResponse (BaseResponse):
    id: int
    email: EmailStr
    created_at: Union[str, None, datetime] = None
