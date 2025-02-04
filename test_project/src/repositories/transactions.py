from src.repositories.base import BaseRepository
from src.models.transactions import TransactionsOrm
from src.repositories.mappers.mappers import TransactionsDataMapper



class TransactionsRepository(BaseRepository):
    model = TransactionsOrm
    mapper = TransactionsDataMapper