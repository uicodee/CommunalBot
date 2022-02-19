from aiogram import Dispatcher

from loader import dp
from .filters import is_verified


if __name__ == "filters":
    dp.filters_factory.bind(is_verified)
