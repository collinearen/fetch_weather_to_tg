import datetime
from engine import engine
from sqlalchemy import insert

import settings
from models import metadata, weather, users


def create_table():
    metadata.create_all(engine)


def drop_tables():
    weather.drop(engine)
    users.drop(engine)


def data_fill():
    for key, values in settings.COORD.items():
        insert_data(town=key, timestamp=datetime.datetime.now(), temp=0)


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

