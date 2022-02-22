from aiogram.dispatcher.filters.state import StatesGroup, State


class AccountEnergy(StatesGroup):
    account_id = State()


class AccountGas(StatesGroup):
    account_id = State()

