from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import Column, Integer, String, Boolean


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None,index=True)

class HeroPublic(HeroBase):
    id: int 

psql_url = 'postgresql://baloo:junglebook@localhost:5432/mkgame'
engine = create_engine(psql_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
