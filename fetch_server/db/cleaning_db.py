import datetime

import settings
from models import Weather, session_engine

def data_fill():
    for key, values in settings.COORD.items():
        insert_data(town=key, timestamp=datetime.datetime.now(), temp=0)


def insert_data(town: str, temp: int, timestamp):
    with session_engine() as session:
        weather = Weather(town=town, temp=temp, timestamp=timestamp)
        session.add(weather)
        session.commit()



    # with engine.connect() as conn:
    #     query = insert(weather).values(
    #         [
    #             {"town": town,
    #              "temp": temp,
    #              "time_stamp": timestamp}
    #         ]
    #     )
    #     conn.execute(query)
    #     conn.commit()
    #     conn.close()
