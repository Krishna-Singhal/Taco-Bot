from pyrogram import filters as rawFilters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from .bot import bot
from .handlers import (start,
                       help,
                       top_tacos,
                       my_tacos,
                       bot_added_handler,
                       incoming_message_handler)
from .callbacks import handle_callback
from .filters import (user_filter,
                      bot_added_filter,
                      taco_filter)

triggers = ['/', '!']

bot.add_handler(MessageHandler(start, user_filter & rawFilters.command("start", triggers)))
bot.add_handler(MessageHandler(help, user_filter
                               & rawFilters.private & rawFilters.command("help", triggers)))
bot.add_handler(MessageHandler(top_tacos,
                               rawFilters.group
                               & user_filter & rawFilters.command("toptacos", triggers)))
bot.add_handler(MessageHandler(my_tacos,
                               rawFilters.group
                               & user_filter & rawFilters.command("mytacos", triggers)))
bot.add_handler(MessageHandler(bot_added_handler,
                               rawFilters.group
                               & rawFilters.new_chat_members & bot_added_filter))
bot.add_handler(MessageHandler(incoming_message_handler,
                               rawFilters.group & user_filter & taco_filter))
bot.add_handler(CallbackQueryHandler(handle_callback))
