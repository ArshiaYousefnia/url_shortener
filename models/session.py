import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    "postgresql://"
    f"{os.getenv("POSTGRES_USER")}:"
    f"{os.getenv("POSTGRES_PASSWORD")}"
    f"@{os.getenv("POSTGRES_HOST")}:"
    f"{os.getenv("POSTGRES_PORT", "5432")}/"
    f"{os.getenv("POSTGRES_DB")}"
)

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
