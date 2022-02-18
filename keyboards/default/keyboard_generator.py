from aiogram import types


def keyboard_generator(row_width: int, data: list, resize_keyboard: bool) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    for item in data:
        keyboard.insert(
            types.KeyboardButton(text=item)
        )

    return keyboard
