import re
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from app.database.queries import set_dream,get_user_id
import app.keyboards.keyboards as kb

add_dream_router = Router()

class AddDream(StatesGroup):
    title = State()
    description = State()
    category = State()
    emotion = State()
    date = State()
    is_repeated = State()

@add_dream_router.message(Command("add_dream"))
async def add_dream(message: Message, state: FSMContext):
    await message.answer("Давай запишем твой сон. Как ты его назовёшь?")
    await state.set_state(AddDream.title)


@add_dream_router.message(AddDream.title)
async def add_dream_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Отлично. А теперь опиши свой сон:")
    await state.set_state(AddDream.description)

@add_dream_router.message(AddDream.description)
async def add_dream_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Выбери категорию сна:", reply_markup=kb.category)
    await state.set_state(AddDream.category)

@add_dream_router.callback_query(AddDream.category)
async def add_dream_category(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(category=callback.data)
    await callback.message.answer("Какая эмоция лучше всего передаёт ощущения от этого сна?", reply_markup=kb.emotions)
    await state.set_state(AddDream.emotion)

@add_dream_router.callback_query(AddDream.emotion)
async def add_dream_emotion(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(emotion=callback.data)
    await callback.message.answer("Укажи дату сна (дд.мм.гггг):")
    await state.set_state(AddDream.date)

@add_dream_router.message(AddDream.date)
async def add_dream_date(message: Message, state: FSMContext):
    while not re.match(r"\d{2}\.\d{2}\.\d{4}", message.text):
        await message.answer("Пожалуйста, укажи дату в формате дд.мм.гггг.")
        return
    await state.update_data(date=message.text)
    await message.answer("Этот сон повторяется время от времени?", reply_markup=kb.repeat)
    await state.set_state(AddDream.is_repeated)

@add_dream_router.callback_query(AddDream.is_repeated)
async def add_dream_repeated(callback:CallbackQuery,state: FSMContext):
    await callback.answer()
    await state.update_data(is_repeated=callback.data)
    data = await state.get_data()
    tg_id = callback.from_user.id
    await set_dream(tg_id,data)
    await callback.message.answer("✅ Сон успешно добавлен в твой архив!\nСпасибо, что поделился им.")
    await state.clear()

