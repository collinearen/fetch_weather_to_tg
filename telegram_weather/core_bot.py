import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import settings
from fetch_server.db.core import create_user, find_user, update_town_for_user, update_time_for_user


# Настройка бота
storage = MemoryStorage()
bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)

# Клавиатура с выбором города
city_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Смоленск'),
            KeyboardButton(text='Москва'),
        ],
        [
            KeyboardButton(text='Санкт-Петербург'),
            KeyboardButton(text='Пермь'),
        ],
    ],
    resize_keyboard=True
)

# Клавиатура с выбором времени
time_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='09:00'),
            KeyboardButton(text='12:00'),
            KeyboardButton(text='15:00'),
        ],
        [
            KeyboardButton(text='18:00'),
            KeyboardButton(text='21:00'),
        ],
    ],
    resize_keyboard=True
)


# Запуск бота

# Обработка команды /start для регистрации пользователя
@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    if find_user(user_id=user_id) is None:
        text = 'Вы уже зарегистрированы!'
    else:
        create_user(user_id=user_id)
        text = ('Вы успешно зарегистрированы!\n'
                'Нажми на /town')

    await message.answer(text)


# Обработка команды /city для выбора города
@dp.message_handler(Command('town'))
async def cmd_city(message: types.Message):
    await message.answer('Выберите город:', reply_markup=city_keyboard)
    # Сохранение состояния пользователя
    await dp.current_state().set_state('town')


# Обработка выбора города
@dp.message_handler(state='town')
async def select_city(message: types.Message, state: FSMContext):
    # Получение выбранного города и сохранение его в базе данных
    town = message.text
    user_id = message.from_user.id

    update_town_for_user(town=town, user_id=user_id)

    await message.answer(f'Отлично, теперь я знаю, где ты живешь)')

    # Запрос на выбор времени
    await message.answer('А теперь выбери время, '
                         'когда тебе присылать сообщения с погодой', reply_markup=time_keyboard)

    # Сохранение состояния пользователя
    await dp.current_state().set_state('time')


# Обработка выбора времени
@dp.message_handler(state='time')
async def select_time(message: types.Message, state: FSMContext):
    # Получение выбранного времени и сохранение его в базе данных
    time = message.text
    user_id = message.from_user.id
    update_time_for_user(user_id=user_id, time=time)

    await message.answer(
        f'Ты выбрал свое время.\n'
        f'Теперь я буду присылать в {time} каждый день какая погода тебя ждет на улице')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    # t.me/collinearen_bot
    asyncio.run(main())
