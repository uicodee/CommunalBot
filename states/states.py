from aiogram.dispatcher.filters.state import StatesGroup, State


class Account(StatesGroup):
    account_id = State()
