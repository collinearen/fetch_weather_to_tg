import asyncio

from sqlalchemy.orm import declarative_base

from weather_database.session import engine

Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def init() -> None:
    await init_models()


if __name__ == '__main__':
    asyncio.run(init())
