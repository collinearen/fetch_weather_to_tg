from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(
    url="postgresql+asyncpg://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)