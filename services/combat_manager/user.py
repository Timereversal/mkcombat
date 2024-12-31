from typing import Union
from datetime import datetime
from pydantic import EmailStr
from  import BaseResponse

class UserResponse(BaseResponse):
    id: int
    email: EmailStr
    created_at : Union(str, None, datetime) = None
