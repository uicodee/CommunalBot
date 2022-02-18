from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import keyboard_generator
from data import buttons


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = keyboard_generator(row_width=3, data=buttons['RU']['main_menu'], resize_keyboard=True)
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=keyboard)
