from fastapi import APIRouter

from src.api.dependencies import DBDep, AdminDep, UserIdDep
from src.schemas.users import UserRequestAdd, UserAdd

router = APIRouter(prefix="/admin", tags=["Админ"])

@router.get("/profile")
async def get_me(
        user_id: UserIdDep,
        db: DBDep,
        _: AdminDep
):
    return await db.users.get_one_or_none(id=user_id)

@router.get("/users")
async def get_users(
        db: DBDep,
        _: AdminDep
):
    return await db.users.get_all_users_with_account()


@router.get("/user/{user_id}")
async def get_one_user(user_id: int, db: DBDep, _: AdminDep):
    return await db.users.get_one_or_none(id=user_id)


@router.post("/user")
async def create_user(
        db: DBDep,
        user_data: UserAdd,
        _: AdminDep
):
    user = await db.users.add(user_data)
    await db.commit()
    return {"status": "OK", "data": user}


@router.put("/user/{user_id}")
async def edit_user(
        user_id: int,
        db: DBDep,
        _: AdminDep,
        user_data: UserAdd,
):
    await db.users.edit(data=user_data, id=user_id)
    await db.commit()
    return {"status": "OK"}


@router.delete("/user/{user_id}")
async def delete_user(
        user_id: int,
        db: DBDep,
        _: AdminDep
):
    await db.users.delete(id=user_id)
    await db.commit()
    return {"status": "OK"}