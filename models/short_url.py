from datetime import datetime

from pydantic import HttpUrl
from sqlmodel import SQLModel, Field


class ShortURL(SQLModel, table=True):
    id: int = Field(primary_key=True)
    url: str = Field(nullable=False, unique=True)
    short_code: str = Field(nullable=False, unique=True)
    access_count: int = Field(nullable=False, default=0)
    created_at: datetime = Field(nullable=False, default_factory=datetime.now)
    updated_at: datetime = Field(nullable=False, default_factory=datetime.now)

class ShortURLCreate(SQLModel):
    url: HttpUrl


class ShortURLPublic(SQLModel):
    id: int
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime

class ShortURLStats(ShortURLPublic):
    access_count: int
