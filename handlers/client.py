from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "В озере 3 рыбы а в машине 5 человек каждый ест банан. Сколько всего пчел в воде?"
    answers = [
        'Ластик',
        '1 пчела',
        'пчелы не летают',
        'спят',
        'пчелы работают и плавать не умеют',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        reply_markup=markup
    )


async def info_handler(message: types.Message):
    await message.reply("Сам рабирайся!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
