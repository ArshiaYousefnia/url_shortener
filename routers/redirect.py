
from fastapi import APIRouter
from starlette.responses import RedirectResponse

from models.session import SessionDep
from routers.shorten import get_short_url_from_db

router = APIRouter()

@router.get("/{short_code}")
async def get_redirect_page(short_code: str, session: SessionDep):
    short = get_short_url_from_db(short_code, session)

    return RedirectResponse(url=short.url)