import re
from random import choice

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import strings
from ..db import database
from ..constants import constants


async def incoming_message_handler(_: Client, message: Message):
    replied = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    receiver = replied.from_user.id
    donating_tacos = len(re.findall('🌮', message.text))

    user_tacos = database.get_user_tacos(chat_id, user_id)
    receiver_tacos = database.get_user_tacos(chat_id, receiver)
    if user_tacos == -1:
        user_tacos = constants.NEW_USER_TACOS
    if receiver_tacos == -1:
        receiver_tacos = constants.NEW_USER_TACOS

    if user_tacos < donating_tacos:
        return await message.reply(
            f"**{strings.NO_TACOS_TEXT}**"
            f"\n`{choice(strings.NOT_ENOUGH)}`"
        )

    database.update_user_tacos(
        chat_id, user_id,
        database.get_collection("CHAT_TACOS"),
        name=message.from_user.first_name,
        username=message.from_user.username or "",
        tacos=user_tacos - donating_tacos
    )
    database.update_user_tacos(
        chat_id, receiver,
        database.get_collection("CHAT_TACOS"),
        name=replied.from_user.first_name,
        username=replied.from_user.username or "",
        tacos=receiver_tacos + donating_tacos
    )

    other_text = message.text.replace('🌮', '')
    out = strings.DONATING_TEXT.format(message.from_user.mention,
                                       donating_tacos, 's' if donating_tacos > 1 else '',
                                       replied.from_user.mention)
    if donating_tacos >= constants.MINIMUM_DONATION:
        extra = choice(strings.DONATING_MORE_THAN_ENOUGH)
    elif donating_tacos == 1:
        extra = choice(strings.DONATING_LESS_THAN_ENOUGH)
    else:
        extra = choice(strings.DONATING_ENOUGH)
    out += "\n`{}`".format(extra)
    if other_text:
        out += "\n**And Said:**\n**>>**: `{}`".format(other_text)
    await message.reply(out,
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                            "Ok", callback_data="ok_{}".format(user_id)
                        )]])
    )
