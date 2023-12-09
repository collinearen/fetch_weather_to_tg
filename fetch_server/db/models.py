import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_async_engine(
    url="postgresql+asyncpg://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)
session_engine = async_sessionmaker(engine)

Base = declarative_base()

intpk = Annotated[int, mapped_column(primary_key=True)]


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[intpk]
    town: Mapped[str] = mapped_column(nullable=False)
    temp: Mapped[int] = mapped_column(default=0)
    time_stamp: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now)",
                            ),
        onupdate=datetime.datetime.now())


class User(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    user_id: Mapped[int]
    town: Mapped[str] = mapped_column(ForeignKey("weather.temp"))
    time_sending: Mapped[str]
