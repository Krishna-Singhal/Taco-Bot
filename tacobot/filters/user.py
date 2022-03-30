from pyrogram import Client, filters as rawFilters
from pyrogram.types import Message


async def user(_, __: Client, message: Message):
    if message.from_user:
        return True
    return False


user_filter = rawFilters.create(user)
