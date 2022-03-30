from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import strings


async def help(_: Client, message: Message):
    await message.reply(strings.HELP_TEXT,
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                            "Ok", callback_data="ok"
                        )]]))
