from aiogram import BaseMiddleware
from aiogram.exceptions import TelegramConflictError
from aiogram.types import Update
from aiogram.dispatcher.dispatcher import Dispatcher
import logging
import asyncio

logger = logging.getLogger(__name__)

class ConflictGuardMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data):
        try:
            return await handler(event, data)
        except TelegramConflictError:
            logger.error("❌ Another instance of the bot is running (polling conflict). Stopping this bot.")
            await asyncio.sleep(1)
            exit(1)
