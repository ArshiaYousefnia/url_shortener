from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from models.session import SessionDep
from models.short_url import ShortURLCreate, ShortURL, ShortURLPublic, ShortURLStats
import secrets

router = APIRouter(
    prefix="/shorten"
)


def get_short_url_from_db(short_code: str, session: SessionDep) -> ShortURL:
    short = session.exec(select(ShortURL).where(ShortURL.short_code == short_code)).first()
    if not short:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return short


@router.post("/", response_model=ShortURLPublic, status_code=status.HTTP_201_CREATED)
async def create_short_url(data: ShortURLCreate, session: SessionDep):
    existing = session.exec(select(ShortURL).where(ShortURL.url == str(data.url))).first()
    if existing:
        raise HTTPException(status_code=409, detail="URL already exists")

    short_code = secrets.token_urlsafe(5)

    new_short_url = ShortURL(
        url=str(data.url),
        short_code=short_code,
    )

    session.add(new_short_url)
    session.commit()
    session.refresh(new_short_url)

    return new_short_url


@router.get("/{short_code}", response_model=ShortURLPublic)
async def get_short_url(short_code: str, session: SessionDep):
    short = get_short_url_from_db(short_code, session)

    short.access_count += 1
    session.add(short)
    session.commit()
    session.refresh(short)

    return short


@router.put("/{short_code}", response_model=ShortURLPublic)
async def update_short_url(data: ShortURLCreate, session: SessionDep, short_code: str):
    short = get_short_url_from_db(short_code, session)

    short.url = str(data.url)
    short.updated_at = datetime.now()

    session.add(short)
    session.commit()
    session.refresh(short)

    return short


@router.delete("/{short_code}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_short_url(short_code: str, session: SessionDep):
    short = get_short_url_from_db(short_code, session)

    session.delete(short)
    session.commit()


@router.get("/{short_code}/stats", response_model=ShortURLStats)
async def get_short_url_stats(short_code: str, session: SessionDep):
    short = get_short_url_from_db(short_code, session)

    return short
