from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import ChannelPrivate

from .. import strings
from ..db import database


async def bot_added_handler(_: Client, message: Message):
    chat_id = message.chat.id
    if chat_id not in database.group_chats:
        database.add_chat(
            database.get_collection("GROUP_CHATS"), chat_id=chat_id
        )
    try:
        await message.reply(
            strings.BOT_ADDED_IN_GROUP_TEXT,
            disable_web_page_preview=True
        )
    except ChannelPrivate:
        pass