import asyncio
import datetime

from sourse import settings
from sourse.fetch_server.weather_database.models import Base as Base_weather
from sourse.fetch_server.weather_database.weather_dao import insert_data
from sourse.telegram_weather.users_database.models import Base as Base_User
from sourse.telegram_weather.users_database.session import engine as engine_user
from weather_database.session import engine as engine_weather


async def init_weather_model():
    async with engine_weather.begin() as conn:
        await conn.run_sync(Base_weather.metadata.drop_all)
        await conn.run_sync(Base_weather.metadata.create_all)


async def data_fill():
    for key, values in settings.COORD.items():
        await insert_data(town=key, temp=0, time_stamp=datetime.datetime.now())


async def init_users_model():
    async with engine_user.begin() as conn:
        await conn.run_sync(Base_User.metadata.drop_all)
        await conn.run_sync(Base_User.metadata.create_all)


async def init() -> None:
    await init_weather_model()
    await init_users_model()
    await data_fill()


if __name__ == '__main__':
    asyncio.run(init())
