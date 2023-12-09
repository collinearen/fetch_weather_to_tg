import datetime

from sqlalchemy import create_engine, insert, update, select

import settings
from .models import metadata, weather, users

engine = create_engine(
    url="postgresql+psycopg2://postgres:0000@0.0.0.0:5432/weather",
    echo=False,
)


def create_table():
    metadata.create_all(engine)


def drop_tables():
    weather.drop(engine)
    users.drop(engine)


#           <----    WEATHER FUNCTIONS   ---->
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


#           <----   USER FUNCTIONS  ---->

def find_user(user_id: int):
    with engine.connect() as conn:
        query = select(users).where(users.c.user_id == user_id)
        try:
            conn.execute(query)
            return 200
        except UserWarning:
            return None
        finally:
            conn.close()


def create_user(user_id: int):
    with engine.connect() as conn:
        query = insert(users).values(
            [
                {
                    "user_id": user_id,
                    "town": "",
                    "time_sending": "",
                }
            ]
        )
        conn.execute(query)
        conn.commit()
        conn.close()


def update_town_for_user(user_id: int, town: str):
    with engine.connect() as conn:
        query = update(users).where(users.c.user_id == user_id).values(
            {
                users.c.town: town,
            }
        )
        conn.execute(query)
        conn.commit()
        conn.close()


def update_time_for_user(user_id: int, time: str):
    with engine.connect() as conn:
        query = update(users).where(users.c.user_id == user_id).values(
            {
                users.c.time_sending: time,
            }
        )
        conn.execute(query)
        conn.commit()
        conn.close()


def show_temperature(user_id: int):
    with engine.connect() as conn:
        try:
            query = select(users).where(users.c.user_id == user_id)
            town_user = conn.execute(query)
            town = town_user.fetchone()[2]

            query = select(weather).where(weather.c.town == town)
            response = conn.execute(query)
            temp = response.fetchone()[2]
            return temp, town
        finally:
            conn.close()


def get_users_for_sending():
    with engine.connect() as conn:
        query = select(users).where(users.c.time_sending == "14:14")
        res = conn.execute(query)
        return res.fetchall()


def start():
    drop_tables()
    create_table()
    data_fill()


if __name__ == '__main__':
    start()