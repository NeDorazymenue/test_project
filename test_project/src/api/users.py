from fastapi import APIRouter

from src.api.dependencies import UserIdDep, DBDep


router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/profile")
async def get_me(
        user_id: UserIdDep,
        db: DBDep,
):
    user = await db.users.get_one_or_none(id=user_id)
    return user


@router.get("/accounts")
async def read_user_accounts(
        user_id: UserIdDep,
        db: DBDep,
):
    return await db.accounts.get_filtered(user_id=user_id)


@router.get("/transactions")
async def read_user_transactions(
        user_id: UserIdDep,
        db: DBDep,
):
    return await db.transactions.get_filtered(user_id=user_id)