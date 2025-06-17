from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Add dream"),KeyboardButton(text="Future dream"),],
    [KeyboardButton(text="Emotion map"),KeyboardButton(text="Dream interpreter"),],
],resize_keyboard=True,one_time_keyboard=True),


category = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🌲 Природа",callback_data="природа"),
        InlineKeyboardButton(text="🏙️ Город  ",callback_data="город")
    ],
    [
        InlineKeyboardButton(text="👥 Люди",callback_data="люди"),
        InlineKeyboardButton(text="👹 Страх",callback_data="страх")
    ],
    [
        InlineKeyboardButton(text="✨ Фантастика",callback_data="фантастика"),
        InlineKeyboardButton(text="🎭 Символика",callback_data="символика")
    ],
])

emotions = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text="😱 Страх",callback_data="страх"),
        InlineKeyboardButton(text="😍 Радость",callback_data="радость")
    ],
    [
        InlineKeyboardButton(text="😭 Грусть",callback_data="грусть"),
        InlineKeyboardButton(text="🤯 Удивление",callback_data="удивление")
    ],
    [
        InlineKeyboardButton(text="😐 Спокойствие",callback_data="спокойствие"),
    ],
])

repeat = InlineKeyboardMarkup(inline_keyboard=
[
    [InlineKeyboardButton(text="🔁 Да ",callback_data="yes")],
    [InlineKeyboardButton(text="❌ Нет",callback_data="no")]
])

emotion = InlineKeyboardMarkup(inline_keyboard=
    [
        [InlineKeyboardButton(text="📆 7 дней",callback_data="period_7")],
        [InlineKeyboardButton(text="📆 30 дней",callback_data="period_30")]
    ]
)

