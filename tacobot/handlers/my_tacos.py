from random import choice

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import strings
from ..db import database
from ..constants import constants


async def my_tacos(_: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    tacos = database.get_user_tacos(chat_id, user_id)
    if tacos == -1:
        tacos = constants.NEW_USER_TACOS
    extra = "\n"
    if tacos > constants.NEW_USER_TACOS:
        extra += f"`{choice(strings.BALANCE_MORE_THAN_ENOUGH)}`"
    elif tacos == constants.NEW_USER_TACOS:
        extra += f"`{choice(strings.BALANCE_ENOUGH)}`"
    elif tacos < constants.NEW_USER_TACOS:
        extra += f"`{choice(strings.BALANCE_LESS_THAN_ENOUGH)}`"
    await message.reply(
        strings.MY_TACOS_TEXT.format(
            message.from_user.mention, tacos, 's' if tacos > 1 else '') + extra,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
            "Ok", callback_data="ok_{}".format(user_id)
        )]])
    )
