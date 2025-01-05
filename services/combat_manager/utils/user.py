from fastapi import HTTPException
from combat_manager.models.user import User
from combat_manager.security import hash_password, verify_password, generate_token
from combat_manager.settings import Settings
from datetime import timedelta

settings = Settings()

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

async def get_login_token(data, session):
    
    user = session.query(User).filter(User.email == data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Email is not registered with uss.")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password.")
    at_payload = {"sub": user.email}
    at_expires = timedelta(minutes=settings.JWT_TOKEN_EXPIRE_MIN)
    access_token = generate_token(at_payload, settings.JWT_SECRET,settings.JWT_ALGORITHM, at_expires )
    return ({"access_token": access_token})

    
    
    