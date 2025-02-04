from src.models.users import UsersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import AdminDataMapper


class AdminsRepository(BaseRepository):
    model = UsersOrm
    mapper = AdminDataMapper