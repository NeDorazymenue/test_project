from src.models.users import UsersOrm
from src.models.accounts import AccountsOrm
from src.models.transactions import TransactionsOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.users import User, UserWithAccounts, UserAdmin
from src.schemas.accounts import Account
from src.schemas.transactions import Transaction


class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = User


class UserDataWithAccountsMapper(DataMapper):
    db_model = UsersOrm
    schema = UserWithAccounts


class AdminDataMapper(DataMapper):
    db_model = UsersOrm
    schema = UserAdmin



class AccountsDataMapper(DataMapper):
    db_model = AccountsOrm
    schema = Account


class TransactionsDataMapper(DataMapper):
    db_model = TransactionsOrm
    schema = Transaction

