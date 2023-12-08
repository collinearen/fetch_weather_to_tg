import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    default="postgresql+psycopg://postgres:0000@0.0.0.0:5432/weather"
)

KEY = os.environ.get("KEY")
