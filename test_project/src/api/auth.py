from fastapi import APIRouter, Body, HTTPException, Response

from src.api.dependencies import UserIdDep, DBDep


from src.schemas.users import UserRequestAdd, UserAdd, UserRequest

from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/register", summary="Регистрация")
async def register_user(
        db: DBDep,
        data: UserRequestAdd = Body(openapi_examples={
    "1": {
        "summary": "Пользователь 1",
        "value": {
            "email" : "user1@user.ru",
            "password" : "usEr_1",
            "full_name": "uSerUserovich"
        }
    },
    "2": {
        "summary": "Пользователь 2",
        "value": {
            "email" : "user2@user.com",
            "password" : "useR_2",
            "full_name": "vtoroyUser"
        }
    }
})):
    password_hash = AuthService().hash_password(data.password)
    new_user_data = UserAdd(email=data.email, password_hash=password_hash, full_name=data.full_name)
    await db.users.add(new_user_data)
    await db.commit()
    return {"status": "OK"}


@router.post("/login", summary="Аутентификация")
async def login_user(
        data: UserRequest,
        response: Response,
        db: DBDep,
):

    user = await db.users.get_user_with_hashed_password(email=data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь с таким email не зарегестрирован")
    if not AuthService().verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Пароль неверный")
    access_token = AuthService().create_access_token({"user_id": user.id})
    response.set_cookie("access_token", access_token)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="access_token")
    return {"status": "OK"}