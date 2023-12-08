import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    default="postgresql+psycopg://postgres:0000@0.0.0.0:5432/weather"
)

KEY = os.environ.get("KEY")

COORD = {
    "Смоленск": "54.46,32.02",
    "Москва": "55.45,37.36",
    "Санкт-Петербург": "59.57,30.19",
    "Пермь": "58.01,56.22"
}
