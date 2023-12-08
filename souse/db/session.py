from sqlalchemy import create_engine, insert

from models import metadata, weather

engine = create_engine(
    url="postgresql+psycopg2://postgres:0000@0.0.0.0:5432/weather",
    echo=True,
)


def create_table():
    metadata.create_all(engine)


def drop_table():
    weather.drop(engine)


def update_data(town: str, temp: str, timestamp: str):
    pass


def insert_data(town: str, temp: str, timestamp: str):
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
    insert_data("Смоленск","f", "ffs")
