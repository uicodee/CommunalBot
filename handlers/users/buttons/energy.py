from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.inline import areas_markup
from data.data import messages


@dp.message_handler(Text(equals='⚡️ Электроэнергия'), state="*")
async def energy(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await message.answer(
        text=messages['RU']['area_request'],
        reply_markup=areas_markup(language="RU")
    )

