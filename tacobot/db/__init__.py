from .db import Database
from ..config import config

database = Database(config.DB_URL, "TacoBot")
