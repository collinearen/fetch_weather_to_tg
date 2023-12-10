import asyncio
import datetime

from sqlalchemy import update

import settings
from .models import Weather, async_session, Base, engine


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def data_fill():
    for key, values in settings.COORD.items():
        await insert_data(town=key, temp=0, time_stamp=datetime.datetime.now())


async def insert_data(town: str, temp: int, time_stamp):
    async with async_session() as session:
        weather = Weather(town=town, temp=temp, time_stamp=time_stamp)
        session.add(weather)
        await session.commit()


async def update_data(town: str, temp: int):
    async with async_session() as session:
        stmt = (
            update(Weather)
            .values(temp=temp,
                    time_stamp=datetime.datetime.now())
            .filter(Weather.town == town)
        )
        await session.execute(stmt)
        await session.commit()


async def init() -> None:
    await init_models()
    await data_fill()


if __name__ == '__main__':
    asyncio.run(init())
