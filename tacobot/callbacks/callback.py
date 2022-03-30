from pyrogram import Client
from pyrogram.types import CallbackQuery


async def handle_callback(_: Client, c: CallbackQuery):
    if c.data == "ok":
        await c.message.delete()
        return
    id = int(c.data.split('_', 1)[1])
    if c.from_user.id == id:
        await c.message.delete()
    else:
        await c.answer("This is not meant for you!")