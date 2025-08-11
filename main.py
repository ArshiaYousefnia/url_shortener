from fastapi import FastAPI
from contextlib import asynccontextmanager
from models import session

from routers import shorten, redirect

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code
    session.create_db_and_tables()
    yield
    # shutdown code

app = FastAPI(lifespan=lifespan)

app.include_router(router=shorten.router)
app.include_router(router=redirect.router)