from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from bot.database.queries import set_user, get_user

class Register(StatesGroup):
    nickname = State()

register_router = Router()

@register_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    await message.answer(
        "👋 Добро пожаловать в Архив Сновидений!\n\n"
        "Я помогу тебе сохранить и изучить твои сны."
    )

    if user is None:
        await message.answer("Давай начнём — выбери ник, под которым ты будешь записывать сны:")
        await state.set_state(Register.nickname)
    else:
        await message.answer(
            "Ты уже зарегистрирован в Архиве Сновидений.\n\n"
            " 📖 Ты можешь:\n\n"
            " 📝 Добавить новый сон — /add_dream\n"
            " 🌌 Посмотреть свои сны — /my_dreams\n"
            " 📊 Узнать карту эмоций — /emotion_map"
        )


@register_router.message(Register.nickname)
async def register(message: Message, state: FSMContext):
    nickname = message.text.strip()

    if not nickname:
        await message.answer("❗ Ник не может быть пустым. Попробуй ещё раз.")
        return

    tg_id = message.from_user.id
    await set_user(tg_id,nickname)

    await message.answer(
        f"✨ Отлично, {nickname}! Ты зарегистрирован в Архиве Сновидений.\n\n"
        " 📖 Ты можешь:\n\n"
        " 📝 Добавить новый сон — /add_dream\n"
        " 🌌 Посмотреть свои сны — /my_dreams\n"
        " 📊 Узнать карту эмоций — /emotion_map"
    )

    await state.clear()





