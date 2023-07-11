import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message

from config import config  # Config
from keyboards.menu import main_menu_command
from keyboards.reply import cats_dogs_keyboard

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет! Кого ты любишь больше, котов или собак?",
                         reply_markup=cats_dogs_keyboard)


@dp.message(Text(text='Собак'))
async def handle_dogs_answer(message: Message):
    await message.answer('Ого, мне тоже. Обожаю их')


@dp.message(Text(text='Котов'))
async def handle_cats_answer(message: Message):
    await message.answer('Интересный выбор. Но мне не нравится')


@dp.message(Command(commands='help'))
async def handle_help(message: Message):
    await message.answer('Типа помощь')


@dp.message(Command('delete_menu'))
async def handle_menu_delete(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Вы удалили меню(((')


async def main():
    try:
        print('Bot Started')
        await bot.set_my_commands(main_menu_command)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')