from src.repositories.users import UsersRepository
from src.repositories.admins import AdminsRepository
from src.repositories.accounts import AccountsRepository
from src.repositories.transactions import TransactionsRepository



class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory


    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = UsersRepository(self.session)
        self.admins = AdminsRepository(self.session)
        self.accounts = AccountsRepository(self.session)
        self.transactions = TransactionsRepository(self.session)
        return self


    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()


    async def commit(self):
        await self.session.commit()