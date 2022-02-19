from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from funcs import db


class Language(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):

        data["language"] = await db.get_language(user_id=message.from_user.id)