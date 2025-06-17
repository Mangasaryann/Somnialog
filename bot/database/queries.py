from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from bot.database.db import async_session
from bot.database.models import User,Category,Dream

async def set_user(tg_id,nickname):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id,nickname=nickname,registration_date=datetime.now()))
            await session.commit()

async def get_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user

async def get_user_id(tg_id):
    async with async_session() as session:
        result = await session.scalar(select(User).where(User.tg_id == tg_id))
        return result.id

async def set_dream(tg_id,data):
    async with async_session() as session:
        category = await session.scalar(select(Category).where(Category.callback_data == data["category"]))
        result = await session.execute(
            select(User).options(selectinload(User.dreams)).where(User.tg_id == tg_id)
        )
        user = result.scalar_one_or_none()
        dreams = Dream(
            user_id=user.id,
            title=data['title'],
            description=data['description'],
            category_id=category.id,
            emotion=data['emotion'],
            date=datetime.strptime(data["date"], "%d.%m.%Y"),
            is_repeated= True if data["is_repeated"] == "yes" else False,
        )
        user.dreams.append(dreams)
        session.add(dreams)
        await session.commit()

async def all_dreams(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            return []

        dreams = await session.scalars(select(Dream).where(Dream.user_id == user.id))
        return dreams.all()

async def get_emotion_stats(tg_id: int, days: int) -> dict:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        result = await session.execute(
            select(Dream.emotion, func.count(Dream.id))
            .where(
                Dream.user_id == user.id,
                Dream.date >= func.date('now', f'-{days} days')
            )
            .group_by(Dream.emotion)
            .order_by(func.count(Dream.id).desc())
        )
        rows = result.all()

    return {row[0]: row[1] for row in rows}