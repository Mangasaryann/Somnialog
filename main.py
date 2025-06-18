import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv

from bot.database.db import create_db
from bot.handlers.add_dream import add_dream_router
from bot.handlers.emotion_map import emotion_map_router
from bot.handlers.my_dreams import my_dreams_router
from bot.handlers.register import register_router
from bot.common.bot_cmds_list import private
from bot.middlewares.conflict_guard import ConflictGuardMiddleware

load_dotenv()

async def main():
    await create_db()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(register_router)
    dp.include_router(add_dream_router)
    dp.include_router(my_dreams_router)
    dp.include_router(emotion_map_router)
    dp.update.outer_middleware(ConflictGuardMiddleware())
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())