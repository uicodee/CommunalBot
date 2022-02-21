from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data import services, welcome, messages
from filters import is_verified, not_verified
from keyboards.default import keyboard_generator
from keyboards.inline import language_markup
from loader import dp


@dp.message_handler(not_verified(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text=welcome,
        reply_markup=await language_markup()
    )


@dp.message_handler(is_verified(), CommandStart())
async def bot_start(message: types.Message, language):
    keyboard = keyboard_generator(row_width=3, data=services[language].keys(), resize_keyboard=True)
    await message.answer(
        text=messages[language]['choose_request'],
        reply_markup=keyboard
    )