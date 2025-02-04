from src.repositories.base import BaseRepository
from src.models.accounts import AccountsOrm
from src.repositories.mappers.mappers import AccountsDataMapper



class AccountsRepository(BaseRepository):
    model = AccountsOrm
    mapper = AccountsDataMapper