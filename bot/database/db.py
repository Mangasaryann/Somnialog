import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from bot.database.models import Base

load_dotenv()

def get_database_url():
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "admin111")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    db = os.getenv("MYSQL_DB", "somnialog")
    return f"mysql+aiomysql://{user}:{password}@{host}:{port}/{db}"

DATABASE_URL = get_database_url()

engine = create_async_engine(
    url=os.getenv("DATABASE_URL"),
    connect_args={"connect_timeout": 10},
    pool_pre_ping=True,)
async_session = async_sessionmaker(engine)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)