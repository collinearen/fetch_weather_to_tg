import asyncio

import aiocron
from aiogram import Bot

from sourse import settings
from users_database.users_dao import chunk_users, show_temperature


class Message(object):
    def __init__(self, bot):
        self.bot = bot

    async def send_weather_05(self):
        # Cписок id-шников пользователей из базы данных
        users = await chunk_users(time_sending="00:39")
        for user in users:
            user_id = user[0]
            sending = await show_temperature(user_id=user_id)
            data = sending
            await self.bot.send_message(user_id, f"{data[0]}, погода сейчас "
                                                 f"{data[1]}℃")

    async def send_weather_07(self):
        # Cписок id-шников пользователей из базы данных
        users = await chunk_users(time_sending="00:38")
        for user in users:
            user_id = user[0]
            sending = await show_temperature(user_id=user_id)
            data = sending
            await self.bot.send_message(user_id, f"{data[0]}, погода сейчас "
                                                 f"{data[1]}℃")

    async def schedule(self):
        aiocron.crontab('39 00 * * *', func=self.send_weather_05)
        aiocron.crontab('38 00 * * *', func=self.send_weather_07)
        while True:
            await asyncio.sleep(1)


if __name__ == '__main__':
    schedule = Message(bot=Bot(settings.TOKEN))
    asyncio.run(schedule.schedule())
