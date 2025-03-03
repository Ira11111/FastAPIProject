from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite+aiosqlite:///./app.db"

engine = create_async_engine(url=DB_URL, echo=True)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

session = async_session()
Base = declarative_base()
