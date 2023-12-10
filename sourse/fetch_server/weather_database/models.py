import datetime

from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(primary_key=True)
    town: Mapped[str] = mapped_column(nullable=False)
    temp: Mapped[int] = mapped_column(default=0)
    time_stamp: Mapped[datetime.datetime] = mapped_column(onupdate=datetime.datetime.now())
