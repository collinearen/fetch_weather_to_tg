import asyncio

from sqlalchemy import update, select

from .models import User
from .session import async_session
from sourse.fetch_server.weather_database.models import Weather


async def create_user(user_id: int):
    async with async_session() as session:
        stmt = select(User.user_id).filter(User.user_id == user_id)
        user_exists = await session.scalar(stmt)
        if user_exists is None:
            session.add(User(user_id=user_id, town="", time_sending=""))
            await session.commit()
            return 0
        else:
            return None


async def update_user(user_id: int, **kwargs):
    async with async_session() as session:
        stmt = update(User).values(kwargs).filter(User.user_id == user_id)
        await session.execute(stmt)
        await session.commit()


async def all_users():
    async with async_session() as session:
        stmt = select(User.user_id)
        res = await session.execute(stmt)
        return res.fetchall()


async def show_temperature(user_id: int):
    async with async_session() as session:
        stmt = select(User.town, Weather.temp).join(Weather, User.town == Weather.town).filter(User.user_id == user_id)
        result = await session.execute(stmt)

        await session.close()
        return result.fetchall()[0]


async def test():
    tst = asyncio.create_task(all_users())
    await asyncio.gather(tst)


if __name__ == '__main__':
    asyncio.run(test())
