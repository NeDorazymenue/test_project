from src.repositories.base import BaseRepository
from src.models.users import UsersOrm
from src.repositories.mappers.mappers import UserDataMapper, UserDataWithAccountsMapper, AdminDataMapper
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from pydantic import EmailStr



from src.schemas.users import UserWithHashedPassword


class UsersRepository(BaseRepository):
    model = UsersOrm
    mapper = UserDataMapper

    async def get_all_users_with_account(self):
        query = (
            select(self.model)
            .filter(self.model.is_admin == False)
            .options(selectinload(self.model.accounts))
        )
        result = await self.session.execute(query)
        users = result.scalars().all()
        return [UserDataWithAccountsMapper.map_to_domain_entity(user) for user in users]

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is None:
            return None
        return UserWithHashedPassword.model_validate(model, from_attributes=True)






