from aiogram import types
from aiogram.dispatcher import FSMContext

from data.data import services, welcome
from keyboards.inline import language_markup
from loader import dp


@dp.message_handler(text=[k[2] for k in [list(j.keys())for j in [services[i] for i in services]]], state="*")
async def energy(message: types.Message, state: FSMContext, language):
    await state.reset_state(with_data=False)
    await message.answer(
        text=welcome,
        reply_markup=await language_markup()
    )

