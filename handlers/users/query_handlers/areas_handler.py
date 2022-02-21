from data import messages, cities
from loader import dp
from aiogram import types
from callback_datas import cb_area
from keyboards.inline import cities_keyboard


@dp.callback_query_handler(cb_area.filter(filter="area"))
async def area_handler(query: types.CallbackQuery, callback_data: dict, language):
    area_id = int(callback_data.get("area_id"))
    await query.message.edit_text(
        text=messages[language]['city_request'],
        reply_markup=cities_keyboard(row_width=2, data=cities[area_id].values())
    )