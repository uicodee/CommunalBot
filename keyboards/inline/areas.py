from aiogram import types
from callback_datas import cb_area


def areas_markup(data: dict, filter: str) -> types.InlineKeyboardMarkup:
    areas_keyboard = types.InlineKeyboardMarkup(row_width=2)
    for area_name, area_id in data.items():
        areas_keyboard.insert(
            types.InlineKeyboardButton(text=area_name, callback_data=cb_area.new(area_id=area_id, filter=filter))
        )

    return areas_keyboard
