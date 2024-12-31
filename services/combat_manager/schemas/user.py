from pydantic import BaseModel,  EmailStr
#import datetime

#validate user form data
class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id:int
    email: EmailStr
#    created_at : datetime
