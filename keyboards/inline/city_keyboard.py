from aiogram import types
from callback_datas import cb_city


def cities_keyboard(row_width: int, data: list) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    for item in data:
        print(item)
        for i, j in item.items():
            keyboard.insert(
                types.InlineKeyboardButton(text=i, callback_data=cb_city.new(city_id=j, filter="city"))
            )

    return keyboard

