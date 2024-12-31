import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime,func
from combat_manager.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    #name=Column(String)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String,  nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    #verified_at = Column(DateTime, nullable=True, default=None)
    #is_active = Column(Boolean, default=False)

    

#class UserCreate(Base):
#   pass

