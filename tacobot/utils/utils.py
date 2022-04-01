import asyncio

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant, FloodWait


async def checkUser(bot: Client, message: Message):
    try:
        await bot.get_chat_member("Ks_Projects", message.from_user.id)
    except UserNotParticipant:
        return False
    except FloodWait as e:
        await message.reply(f"Please wait for {time_formatter(e.x * 1000)}")
        await asyncio.sleep(e.x)
        return await checkUser(message)
    else:
        return True


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
          ((str(hours) + "h, ") if hours else "") + \
          ((str(minutes) + "m, ") if minutes else "") + \
          ((str(seconds) + "s, ") if seconds else "") + \
          ((str(milliseconds) + "ms") if milliseconds else "")
    return tmp[:-2]
