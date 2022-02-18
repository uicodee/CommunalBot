from aiogram.dispatcher import FSMContext

from data import errors
from funcs import get_info
from loader import dp
from aiogram import types
from states import Account


@dp.message_handler(state=Account.account_id)
async def get_account(message: types.Message, state: FSMContext):
    account_id = message.text
    city_code = (await state.get_data()).get('city_code')
    if not account_id.isdigit():
        await message.answer(
            text=errors['RU']['digit_error']
        )
    else:
        await get_info(city_code=city_code, account_id="0071177")