from aiogram import types
from aiogram.dispatcher import FSMContext

from data.data import messages, areas, services
from keyboards.inline import areas_markup
from loader import dp


@dp.message_handler(text=[k[0] for k in [list(j.keys())for j in [services[i] for i in services]]], state="*")
async def energy(message: types.Message, state: FSMContext, language):
    await state.reset_state(with_data=False)
    await message.answer(
        text=messages[language]['area_request'],
        reply_markup=areas_markup(data=areas[language], filter="energy")
    )

