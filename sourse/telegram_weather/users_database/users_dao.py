from sqlalchemy import insert, update, select


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
        query = select(users).where(users.c.user_id == user_id)
        town_user = conn.execute(query)
        town = town_user.fetchone()[2]

        query = select(weather).where(weather.c.town == town)
        response = conn.execute(query)
        temp = response.fetchone()[2]
        conn.close()
        return temp, town


def get_users_for_sending():
    with engine.connect() as conn:
        query = select(users).where(users.c.time_sending == "15:00")
        res = conn.execute(query)
        conn.close()
    return res.fetchall()


def find_user(user_id: int):
    with engine.connect() as conn:
        query = select(users).filter(users.c.user_id == user_id)
        res = conn.execute(query)
        conn.close()
    return res.fetchone()