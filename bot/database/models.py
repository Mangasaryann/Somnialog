from datetime import datetime,date
from sqlalchemy import BigInteger, String, DateTime, ForeignKey, Text, Boolean, Integer, Date
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__ = "users"
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    nickname: Mapped[str] = mapped_column(String(25), nullable=False)
    registration_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    dreams = relationship("Dream", back_populates="user", lazy="selectin")

class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
    callback_data: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)

class Dream(Base):
    __tablename__ = "dreams"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="dreams")
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    emotion: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    is_repeated: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

class EmotionStatistic(Base):
    __tablename__ = "emotions_statistics"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    emotion: Mapped[str] = mapped_column(String(10), nullable=False)
    count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
