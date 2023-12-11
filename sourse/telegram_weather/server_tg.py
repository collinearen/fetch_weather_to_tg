import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from sourse import settings
from users_database.users_dao import update_user, create_user


class WeatherBot:
    def __init__(self, token):
        self.token = token
        self.storage = MemoryStorage()
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(bot=self.bot, storage=self.storage)
        self.city_keyboard = ReplyKeyboardMarkup(
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
            resize_keyboard=True,
            one_time_keyboard=True
        )
        self.time_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='00:39'),
                    KeyboardButton(text='00:38'),
                    KeyboardButton(text='23:59'),
                ],
                [
                    KeyboardButton(text='00:00'),
                    KeyboardButton(text='21:00'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        self.dp.register_message_handler(self.cmd_start, commands='start')
        self.dp.register_message_handler(self.cmd_city, commands='town')
        self.dp.register_message_handler(self.select_city, state='town')
        self.dp.register_message_handler(self.select_time, state='time')

    async def start(self):
        logging.basicConfig(level=logging.INFO)
        await self.dp.start_polling()

    async def cmd_start(self, message: types.Message):
        user_id = message.from_user.id
        if await create_user(user_id=user_id) is None:
            text = (f"Добро пожаловать!"
                    f"\nЖмякай на /town")
        else:
            text = ("Вы успешно зарегистрировались!"
                    "\nЖмякайте на /town")
        await message.answer(text)

    async def cmd_city(self, message: types.Message):
        await message.answer('Выбери город', reply_markup=self.city_keyboard)
        await self.dp.current_state().set_state('town')

    async def select_city(self, message: types.Message, state: FSMContext):
        town = message.text
        user_id = message.from_user.id
        await update_user(user_id=user_id, town=town)
        await message.answer(f'Отлично, теперь я знаю, где ты живешь)')
        await message.answer('А теперь выбери время, '
                             'когда тебе присылать сообщения с погодой', reply_markup=self.time_keyboard)
        await self.dp.current_state().set_state('time')

    async def select_time(self, message: types.Message, state: FSMContext):
        time_sending = message.text
        user_id = message.from_user.id
        await update_user(user_id=user_id, time_sending=time_sending)
        await message.answer(
            f'Ты выбрал свое время.\n'
            f'Теперь я буду присылать в {time_sending} каждый день какая погода тебя ждет на улице')

    async def main(self):
        await self.start()


if __name__ == '__main__':
    bot = WeatherBot(token=settings.TOKEN)
    asyncio.run(bot.main())
