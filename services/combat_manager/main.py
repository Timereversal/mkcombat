
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Query
#from heroes import create_db_and_tables, Hero, SessionDep, HeroPublic
#import models
from combat_manager.database import engine

from combat_manager.routes import user



def create_application():
    application = FastAPI()
    application.include_router(user.user_router)
    return application

app = create_application()
#models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {'Hello': "World"}


@app.get("/register")
def user_register():
    return {'Hello': "World"}

