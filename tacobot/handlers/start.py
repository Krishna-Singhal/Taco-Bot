from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import strings
from ..utils import checkUser
from ..db import database


async def start(bot: Client, message: Message):
    if message.chat.type == "private":
        if not await checkUser(bot, message):
            return await message.reply(
                "You have not joined @Ks_Projects, join this channel and start again.",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Join Now", url="https://t.me/Ks_Projects")]]
                )
            )
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
