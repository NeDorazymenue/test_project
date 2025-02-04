from fastapi import HTTPException, Request

from typing import Annotated
from fastapi import Query, Depends

from src.database import async_session_maker
from src.services.auth import AuthService
from src.utils.db_manager import DBManager
from src.schemas.users import User





async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]


def get_token(request: Request) -> str:
    token = request.cookies.get("access_token", None)
    if not token:
        raise HTTPException(status_code=401, detail="Вы не предоставили токен доступа")
    return token


def get_current_user_id(token: str = Depends(get_token)) -> int:
    data = AuthService().decode_token(token)
    return data["user_id"]


UserIdDep = Annotated[int, Depends(get_current_user_id)]


async def require_admin(user_id: UserIdDep, db: DBDep):

    user = await db.admins.get_one_or_none(id=user_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Недостаточно прав")

AdminDep = Annotated[None, Depends(require_admin)]


