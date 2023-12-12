import datetime

from sqlalchemy import update

from sourse import settings
from .models import Weather
from .session import async_session


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
