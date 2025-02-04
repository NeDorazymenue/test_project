from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


engine = create_async_engine(settings.db_url, echo=True)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass