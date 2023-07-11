from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

answer_dogs_button = KeyboardButton(text='Собак')  # Кнопка
answer_cats_button = KeyboardButton(text='Котов')  # Кнопка

cats_dogs_keyboard = ReplyKeyboardMarkup(keyboard=[
    [answer_dogs_button, answer_cats_button],
], resize_keyboard=True)  # Клавиатура