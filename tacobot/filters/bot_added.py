from pyrogram import Client, filters as rawFilters
from pyrogram.types import Message


async def bot_added(_, __: Client, message: Message):
    for user in message.new_chat_members:
        if user.is_self:
            return True
    return False


bot_added_filter = rawFilters.create(bot_added)
