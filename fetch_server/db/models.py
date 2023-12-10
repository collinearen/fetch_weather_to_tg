import datetime
from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_async_engine(
    url="postgresql+asyncpg://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

int_pk = Annotated[int, mapped_column(primary_key=True)]


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int_pk]
    town: Mapped[str] = mapped_column(nullable=False)
    temp: Mapped[int] = mapped_column(default=0)
    time_stamp: Mapped[datetime.datetime] = mapped_column(onupdate=datetime.datetime.now())


class User(Base):
    __tablename__ = "users"
    id: Mapped[int_pk]
    user_id: Mapped[int]
    town: Mapped[str]
    time_sending: Mapped[str]
