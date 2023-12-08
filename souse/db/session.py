import datetime

from sqlalchemy import create_engine, insert, update

import settings
from .models import metadata, weather

engine = create_engine(
    url="postgresql+psycopg2://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)


def create_table():
    metadata.create_all(engine)


def drop_table():
    weather.drop(engine)


def data_fill():
    for key, values in settings.COORD.items():
        insert_data(town=key, timestamp=datetime.datetime.now(), temp=0)


def update_data(town: str, temp: int, timestamp):
    with engine.connect() as conn:
        query = update(weather).where(weather.c.town == town).values(
            {
                weather.c.temp: temp,
                weather.c.time_stamp: timestamp
            }
        )
        conn.execute(query)
        conn.commit()
        conn.close()


def insert_data(town: str, temp: int, timestamp):
    with engine.connect() as conn:
        query = insert(weather).values(
            [
                {"town": town,
                 "temp": temp,
                 "time_stamp": timestamp}
            ]
        )
        conn.execute(query)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    drop_table()
    create_table()
    data_fill()
