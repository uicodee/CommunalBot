from aiogram.dispatcher import FSMContext

from data import messages
from funcs import get_info
from loader import dp
from aiogram import types
from callback_datas import cb_city
from states import Account


@dp.callback_query_handler(cb_city.filter(filter="city"))
async def cities_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext, language):
    city_code = callback_data.get("city_id")
    await query.message.edit_text(
        text=messages[language]['account_id']
    )
    await state.update_data(city_code=city_code)
    await Account.account_id.set()
