from os import environ as env, path
from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")


class config:
    API_ID = int(env.get("API_ID")) or 0
    API_HASH = env.get("API_HASH")
    BOT_TOKEN = env.get("BOT_TOKEN")
    DB_URL = env.get("DATABASE_URL")
