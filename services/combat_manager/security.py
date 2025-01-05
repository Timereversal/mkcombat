from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
import jwt
from combat_manager.models.user import User
from fastapi import HTTPException,status

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password):      
    return pwd_context.hash(password)

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)


def generate_token(payload: dict, secret: str, algo: str, expiry: timedelta):
    expire = datetime.now(timezone.utc) + expiry
    payload.update({"exp": expire})
    return jwt.encode(payload, secret , algorithm=algo)

def get_token_user(token: str, db):
    payload = get_token_payload(token, settings.JWT_SECRET, settings.JWT_ALGORITHM)
    if payload:
        user: str = payload.get("sub") 
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate":"Bearer"},
            )
        try:
            us = db.Query(User).filter(User.email==user).first()
        except Exception as user_exec:
            us = None
        return us
        
        

def get_token_payload(token: str, secret: str, algo: str):
    try:
        payload = jwt.decode(token, secret, algo)
    except Exception as jwt_exec:
        payload = None