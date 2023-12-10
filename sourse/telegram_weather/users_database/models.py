from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_async_engine(
    url="postgresql+asyncpg://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    town: Mapped[str]
    time_sending: Mapped[str]
