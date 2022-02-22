from data import services, messages
from keyboards.default import keyboard_generator
from loader import dp
from aiogram import types
from callback_datas import cb_language
from funcs import db


@dp.callback_query_handler(cb_language.filter())
async def language_handler(query: types.CallbackQuery, callback_data: dict):
    await query.message.delete()
    language = callback_data.get("language")
    if await db.user(user_id=query.from_user.id) is False:
        await db.new(
            user_id=query.from_user.id,
            firstname=query.from_user.full_name,
            language=callback_data.get("language")
        )
    else:
        await db.update_language(user_id=query.from_user.id, language=language)
    keyboard = keyboard_generator(row_width=2, data=services[language].keys(), resize_keyboard=True)
    await query.message.answer(
        text=messages[language]['choose_request'],
        reply_markup=keyboard
    )
