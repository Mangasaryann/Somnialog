
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.database.queries import all_dreams

my_dreams_router = Router()

@my_dreams_router.message(Command("my_dreams"))
async def my_dreams(message: Message):
    dreams = await all_dreams(message.from_user.id)
    print(dreams)
    if dreams:
        for dream in dreams:
            await message.answer(f"Название: {dream.title} \n\n"
                             f"Описаниее: {dream.description}\n"
                             f"emotion: {dream.emotion}\n"
                             f"date: {dream.date}\n"
                             f"is_repeated: {dream.is_repeated}")
    else:
        await message.answer("list is empty")