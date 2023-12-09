import asyncio
import datetime

import settings
from models import Weather, session_engine, Base, engine


async def create_tables():
    await Base.metadata.drop_all(engine)


async def data_fill():
    for key, values in settings.COORD.items():
        await insert_data(town=key, temp=0, time_stamp=datetime.datetime.now(), )


async def insert_data(town: str, temp: int):
    async with session_engine() as session:
        weather = Weather(town=town, temp=temp)
        session.add(weather)
        await session.commit()


if __name__ == '__main__':
    asyncio.run(create_tables())
    # with engine.connect() as conn:
    #     query = insert(weather).values(
    #         [
    #             {"town": town,
    #              "temp": temp,
    #              "time_stamp": timestamp}
    #         ]
    #     )
    #     conn.execute(query)
    #     conn.commit()
    #     conn.close()
