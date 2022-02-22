import datetime

from aiogram.dispatcher import FSMContext

from data import errors, messages
from funcs import electricity_info, gas_info
from loader import dp
from aiogram import types
from states import AccountEnergy, AccountGas


@dp.message_handler(state=AccountEnergy.account_id)
async def get_account(message: types.Message, state: FSMContext, language):
    account_id = message.text
    city_code = (await state.get_data()).get('city_code')
    if not account_id.isdigit():
        await message.answer(
            text=errors['RU']['digit_error']
        )
    else:
        msg = await message.answer(
            text="⏳"
        )
        data = await electricity_info(city_code=city_code, account_id=account_id)
        await dp.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg.message_id,
            text=messages[language]['electricity'].format(
                service=data[0]['Оплата услуги:'],
                name=data[10]['Ф.И.О.'],
                region=data[1]['Регион'],
                code=data[2]['Район'],
                account_id=data[3]['На счет:'],
                operator=data[5]['Оператор'],
                time=datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
                balance=data[12]['Сальдо'],
                last_pay=data[13]['Дата посл. платежа'],
                last_pay_count=data[14]['Последний платёж'],
            )
        )
    await state.reset_state(with_data=True)


@dp.message_handler(state=AccountGas.account_id)
async def get_account(message: types.Message, state: FSMContext, language):
    account_id = message.text
    city_code = (await state.get_data()).get('city_code')
    if not account_id.isdigit():
        await message.answer(
            text=errors[language]['digit_error']
        )
    else:
        msg = await message.answer(
            text="⏳"
        )
        data = await gas_info(city_code=city_code, account_id=account_id)
        await dp.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg.message_id,
            text=messages[language]['gas'].format(
                service=data[0]['Оплата услуги:'],
                name=data[9]['ФИО абонента'],
                region=data[1]['Регион'],
                code=data[2]['Филиал'],
                account_id=data[3]['На счет:'],
                address=data[10]['Адрес'],
                operator=data[6]['Оператор'],
                period=data[11]['Период'],
                time=datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
                count_now=data[13]['Пок.счетчика'],
                count_until=data[17]['Расчет.показ.'],
                start_balance=data[12]['Сальдо на нач.'],
                end_balance=data[16]['Сальдо на конец']
            )
        )
    await state.reset_state(with_data=True)
