from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import strings
from ..db import database
from ..constants import constants


async def top_tacos(bot: Client, message: Message):
    chat_id = message.chat.id
    data = database.get_top_tacos(chat_id)
    if len(data) < 5:
        members = await bot.get_chat_members(chat_id, limit=5 - len(data))
        for member in members:
            if member.user.is_bot or member.user.id in [a['user_id'] for a in data]:
                continue
            database.update_user_tacos(chat_id,
                                       member.user.id,
                                       database.get_collection("CHAT_TACOS"),
                                       name=member.user.first_name,
                                       username=member.user.username or "",
                                       tacos=constants.NEW_USER_TACOS)
            data.append({"user_id": member.user.id,
                         "name": member.user.first_name,
                         "username": member.user.username or "",
                         "tacos": constants.NEW_USER_TACOS})
    out = f"**{strings.TOP_TACOS_TEXT.format(len(data))}**"
    for i, d in enumerate(data, start=1):
        if d["username"]:
            name = f"[{d['username']}](https://t.me/{d['username']})"
        else:
            name = f"[{d['name']}](tg://user?id={d['user_id']})"
        out += f"\n{i}. {name} - `{d['tacos']}` tacos!"
    await message.reply(out,
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                            "Ok", callback_data="ok_{}".format(message.from_user.id)
                        )]]))
