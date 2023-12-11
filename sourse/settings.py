import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    default="postgresql+psycopg://postgres:0000@0.0.0.0:5432/weather"
)

KEY = os.environ.get("KEY")

COORD = {
    "Смоленск": "54.7818,32.0401",
    "Москва": "55.45,37.36",
    "Санкт-Петербург": "59.93428,30.3351",
    "Пермь": "58.010455,56.229443",
    "Сафоново": "55.1068,33.2400",
    "Мурманск": "68.95852,33.08266 ",
    "Вашингтон": "38.90719,-77.03687 ",
}

TOKEN = os.environ.get("TOKEN")

COLLECTOR_PATH = os.environ.get("COLLECTOR_PATH")
BOT_PATH = os.environ.get("BOT_PATH")
