from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    full_name: Mapped[str] = mapped_column(String(100))
    is_admin: Mapped[bool] = mapped_column(default=False)
    accounts: Mapped[list["AccountsOrm"]] = relationship(
        "AccountsOrm", back_populates="users", lazy="selectin"
    )
    transactions: Mapped[list["TransactionsOrm"]] = relationship(
        "TransactionsOrm", back_populates="users", lazy="selectin"
    )