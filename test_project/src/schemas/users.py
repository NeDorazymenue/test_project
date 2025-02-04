from pydantic import BaseModel, EmailStr
from src.schemas.accounts import Account


class UserRequestAdd(BaseModel):
    email: EmailStr
    password: str
    full_name: str


class UserRequest(BaseModel):
    email: EmailStr
    password: str


class UserAdd(BaseModel):
    email: EmailStr
    password_hash: str
    full_name: str


class User(BaseModel):
    id: int
    email: EmailStr
    full_name: str


class UserAdmin(User):
    is_admin: bool



class UserWithHashedPassword(User):
    password_hash: str


class UserWithAccounts(User):
    accounts: list[Account]



