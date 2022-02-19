from aiogram import types
from data.data import languages
from callback_datas import cb_language


async def language_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for language, code in languages.items():
        keyboard.insert(
            types.InlineKeyboardButton(text=language, callback_data=cb_language.new(language=code))
        )

    return keyboard
