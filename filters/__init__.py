from aiogram import Dispatcher

from loader import dp
from .filters import is_verified, not_verified


if __name__ == "filters":
    dp.filters_factory.bind(is_verified)
    dp.filters_factory.bind(not_verified)
