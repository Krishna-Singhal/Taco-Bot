from pyrogram import Client
from pyrogram.types import Message

from .. import strings
from ..db import database


async def start(_: Client, message: Message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        if chat_id not in database.user_chats:
            database.add_chat(
                database.get_collection("USER_CHATS"), user_id=chat_id
            )
    else:
        if chat_id not in database.group_chats:
            database.add_chat(
                database.get_collection("GROUP_CHATS"), chat_id=chat_id
            )
    await message.reply(strings.START_TEXT, disable_web_page_preview=True)
