from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import strings
from ..utils import checkUser


async def help(bot: Client, message: Message):
    #if not await checkUser(bot, message):
        #return await message.reply(
            #"You have not joined @Ks_Projects, join this channel and start again.",
            #reply_markup=InlineKeyboardMarkup(
                #[[InlineKeyboardButton("Join Now", url="https://t.me/Ks_Projects")]]
            #)
        #)
    await message.reply(strings.HELP_TEXT,
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                            "Ok", callback_data="ok"
                        )]]))
