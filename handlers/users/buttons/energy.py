from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from keyboards.inline import areas_markup
from data.data import messages, buttons


@dp.message_handler(text=[j[0] for j in [buttons[i]['main_menu'] for i in buttons]], state="*")
async def energy(message: types.Message, state: FSMContext, language):
    await state.reset_state(with_data=False)
    await message.answer(
        text=messages[language]['area_request'],
        reply_markup=areas_markup(language=language)
    )

