import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from bot.database.models import Base

load_dotenv()

engine = create_async_engine(url=os.getenv("DATABASE_URL"),echo=True)
async_session = async_sessionmaker(engine)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)