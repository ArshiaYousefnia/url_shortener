from fastapi import FastAPI
from contextlib import asynccontextmanager
from models import session

import routers.short_urls

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code
    session.create_db_and_tables()
    yield
    # shutdown code

app = FastAPI(lifespan=lifespan)

app.include_router(router=routers.short_urls.router)
