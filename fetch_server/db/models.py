import datetime

from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine(
    url="postgresql+psycopg2://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)
session_engine = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(primary_key=True)
    town: Mapped[str] = mapped_column(nullable=False)
    temp: Mapped[int] = mapped_column(default=0)
    time_stamp: Mapped[DateTime] = mapped_column(timezone=True, onupdate=datetime.datetime.now())


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    town: Mapped[str] = mapped_column(nullable=False)
    time_sending: Mapped[str]
