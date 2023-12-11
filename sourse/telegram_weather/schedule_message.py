import asyncio

import aiocron
from aiogram import Bot

from sourse import settings
from users_database.users_dao import chunk_users, show_temperature


class Message(object):
    def __init__(self, bot):
        self.bot = bot

    async def send_weather_at_08(self):
        # Cписок id-шников пользователей из базы данных
        users = await chunk_users(time_sending="08:00")
        for user in users:
            user_id = user[0]
            sending = await show_temperature(user_id=user_id)
            data = sending
            await self.bot.send_message(user_id, f"{data[0]}, погода сейчас "
                                                 f"{data[1]}℃")

    async def send_weather_at_12(self):
        # Cписок id-шников пользователей из базы данных
        users = await chunk_users(time_sending="12:00")
        for user in users:
            user_id = user[0]
            sending = await show_temperature(user_id=user_id)
            data = sending
            await self.bot.send_message(user_id, f"{data[0]}, погода сейчас "
                                                 f"{data[1]}℃")

    async def send_weather_at_16(self):
        # Cписок id-шников пользователей из базы данных
        users = await chunk_users(time_sending="16:00")
        for user in users:
            user_id = user[0]
            sending = await show_temperature(user_id=user_id)
            data = sending
            await self.bot.send_message(user_id, f"{data[0]}, погода сейчас "
                                                 f"{data[1]}℃")

    async def send_weather_at_20(self):
        # Cписок id-шников пользователей из базы данных
        users = await chunk_users(time_sending="20:00")
        for user in users:
            user_id = user[0]
            sending = await show_temperature(user_id=user_id)
            data = sending
            await self.bot.send_message(user_id, f"{data[0]}, погода сейчас "
                                                 f"{data[1]}℃")

    async def schedule(self):
        aiocron.crontab('00 08 * * *', func=self.send_weather_at_08)
        aiocron.crontab('00 12 * * *', func=self.send_weather_at_12)
        aiocron.crontab('00 16 * * *', func=self.send_weather_at_16)
        aiocron.crontab('00 20 * * *', func=self.send_weather_at_20)
        while True:
            await asyncio.sleep(1)


if __name__ == '__main__':
    schedule = Message(bot=Bot(settings.TOKEN))
    asyncio.run(schedule.schedule())
