from aiogram import types
from data.data import areas
from callback_datas import cb_area


def areas_markup(language: str) -> types.ReplyKeyboardMarkup:
    areas_keyboard = types.InlineKeyboardMarkup(row_width=2)
    for area_name, area_id in areas[language].items():
        areas_keyboard.insert(
            types.InlineKeyboardButton(text=area_name, callback_data=cb_area.new(area_id=area_id, filter="area"))
        )

    return areas_keyboard
