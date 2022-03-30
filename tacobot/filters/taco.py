import re

from pyrogram import Client, filters as rawFilters
from pyrogram.types import Message


async def taco(_, __: Client, message: Message):
    if (
        not message.from_user.is_bot
        and not message.service
        and not message.outgoing
        and not message.forward_date
        and not message.edit_date
        and message.reply_to_message
        and message.reply_to_message.from_user
        and not message.reply_to_message.from_user.is_bot
        and not message.from_user.id == message.reply_to_message.from_user.id
        and message.text
        and len(re.findall('🌮', message.text)) > 0
    ):
        return True
    return False


taco_filter = rawFilters.create(taco)
