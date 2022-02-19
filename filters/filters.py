from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from funcs import db


class is_verified(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if await db.user(user_id=message.from_user.id):
            return True
        else:
            return False
