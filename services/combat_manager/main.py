from typing import Union
from fastapi import FastAPI
from heroes import create_db_and_tables

app = FastAPI()

@app.get("/")
def read_root():
    return {'Hello': "World"}


@app.get("/register")
def user_register():
    return {'Hello': "World"}

@app.get("/startup")
def on_startup():
    print("test")
    create_db_and_tables()

