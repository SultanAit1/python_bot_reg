from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp



@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Ок очень простой вопрос" \
               "Как создать вечный двигатель?"
    answers = [
        "Не знаю",
        "Никак",
        "Я верующий",
        "Можно но нам это не нужно",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )

@dp.callback_query_handler(text="button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="button_call_3")
    markup.add(button_call_1)

    question = "Какие авиакомпании лучше?"
    answers = [
        "авиасейлс",
        "aviasales",
        "первый вариант",
        "второй вариант",
        "Все вместе",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        reply_markup=markup
    )

@dp.message_handler(commands=['mem'])
async def send_image(message: types.Message):
    photo = open('media/mem1.jpg', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_3")