import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import text


logging.basicConfig(level=logging.INFO)

bot = Bot(token="5882986304:AAGnSYrPqqEotVJyTrH9J7JEcFLmu4Lymo0")

dp = Dispatcher(bot)


@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    answer = text(
        "Hello, I'm simple button bot, Laba Botovich", sep="\n")
    await message.answer(answer, parse_mode="MARKDOWN")


@dp.message(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer("Меню")


@dp.message()
async def button_handler(message: types.Message):
    mes = message.text

    if mes == "Начать":
        await message.answer("Начинаем")
    elif mes == "Закончить":
        await message.answer("Заканчиваем")
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup_btn_1 = types.KeyboardButton("Начать")
        markup_btn_2 = types.KeyboardButton("Закончить")
        markup.add(markup_btn_1, markup_btn_2)
        await message.answer("Пожалуйста, нажмите кнопку", markup)


async def main():
    await dp.start_polling(bot)
