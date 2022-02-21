from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from funcs import db


class Language(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        try:
            language = (await db.get_language(user_id=message.from_user.id))['language']
        except TypeError:
            language = message.from_user.locale.language
        data["language"] = language

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        try:
            language = (await db.get_language(user_id=callback_query.from_user.id))['language']
        except TypeError:
            language = callback_query.from_user.locale.language
        data["language"] = language
