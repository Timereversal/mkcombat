from fastapi import HTTPException
from combat_manager.models.user import User
from combat_manager.security import hash_password

async def create_user_account(data, session):

    user_exist = session.query(User).filter(User.email == data.email).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="Email is already exists.")
    user = User()
    user.email = data.email
    user.password = hash_password(data.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
    
    