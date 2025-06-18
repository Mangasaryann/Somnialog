from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import bot.keyboards.keyboards as kb
from bot.database.queries import get_emotion_stats
emotion_map_router = Router()

@emotion_map_router.message(Command("emotion_map"))
async def emotion_map_command(message: Message):
    await message.answer("Выбери период:", reply_markup=kb.emotion)

@emotion_map_router.callback_query(F.data.startswith("period_"))
async def show_emotion_map(callback: CallbackQuery):
    period = callback.data.split("_")[1]
    tg_id = callback.from_user.id

    emotions = await get_emotion_stats(tg_id, int(period))
    if emotions:
        result = "📝 Вот твоя карта эмоций за последние {} дней:\n\n".format(period)
        for emoji, count in emotions.items():
            result += f"{emoji} — {count}\n"
    else:
        result = "😐 У тебя пока нет снов за этот период."

    await callback.message.answer(result)
    await callback.answer()