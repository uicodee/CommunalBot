from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import keyboard_generator
from keyboards.inline import language_markup
from data import buttons, welcome, messages
from filters import is_verified


@dp.message_handler(is_verified(), CommandStart())
async def bot_start(message: types.Message, language):
    keyboard = keyboard_generator(row_width=3, data=buttons[language]['main_menu'], resize_keyboard=True)
    await message.answer(
        text=messages[language]['choose_request'],
        reply_markup=keyboard
    )


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text=welcome,
        reply_markup=await language_markup()
    )
