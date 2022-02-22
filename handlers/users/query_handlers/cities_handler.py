from aiogram.dispatcher import FSMContext

from data import messages
from loader import dp
from aiogram import types
from callback_datas import cb_city
from states import AccountEnergy, AccountGas


@dp.callback_query_handler(cb_city.filter(filter="energy"))
async def cities_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext, language):
    city_code = callback_data.get("city_id")
    await query.message.edit_text(
        text=messages[language]['account_id']
    )
    await state.update_data(city_code=city_code)
    await AccountEnergy.account_id.set()


@dp.callback_query_handler(cb_city.filter(filter="gas"))
async def cities_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext, language):
    city_code = callback_data.get("city_id")
    await query.message.edit_text(
        text=messages[language]['account_id']
    )
    await state.update_data(city_code=city_code)
    await AccountGas.account_id.set()
