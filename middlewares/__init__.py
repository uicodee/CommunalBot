from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .language import Language


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Language())
