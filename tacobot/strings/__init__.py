from pyrogram.types import InlineKeyboardMarkup as i, InlineKeyboardButton as b

START_TEXT = """
**Hello, my name is TacoBot and my sole purpose is to help you spread appreciation, celebrate, and have a little fun.**

Simply add me to your group and you’ll be giving tacos in no time! You can also send me /help to read about my abilities :^)
"""
HELP_TEXT = """
**This is what i can do now:**

/toptacos - `shows top-5 Taco'ers in group chat (only in groups)`

/mytacos - `shows your taco-balance (only in groups)`
"""
BOT_ADDED_IN_GROUP_TEXT = """
**Thanks for adding me!**

From this moment I'm counting  all  tacos for  all  members in this chat. You can share tacos by replying to other user's messages with taco-emoji (🌮).
**Every user gets `{}` tacos.**

**This is what i can do now:**

/toptacos - `shows top-5 Taco'ers in current chat (only in groups)`

/mytacos - `shows your taco-balance (only in groups)`

`P.S. Again, only if you gave me access to messages❤️`
"""

MARKUP = i([[b("Updates Channel 🔊", url="https://t.me/Ks_Projects"), b("Vote me 5 ⭐", url="https://t.me/BotsArchive/2383")]])

TOP_TACOS_TEXT = "Here are the top-{} taco-owners of this chat!"
MY_TACOS_TEXT = "{} **has `{}` taco{} on their taco-balance.**"
DONATING_TEXT = "{} **gave `{}` taco{} to** {}!"
NO_TACOS_TEXT = "Whoops! You don't have enough taco to donate!"

BALANCE_MORE_THAN_ENOUGH = ["WoW, I'm impressed! How did you earn so many tacos? Are you trading crypto or what?🙀"]
BALANCE_ENOUGH = ["I guess, you dont gift much of your tacos... and so do your neighbours 😪"]
BALANCE_LESS_THAN_ENOUGH = ["Where did all your tacos go?!! 👿👿👿"]
NOT_ENOUGH = ["You can probably start some crowdfunding page to get some tacos from your friends and other participants 🙃"]

DONATING_LESS_THAN_ENOUGH = ["Why didn't you share more tacos tho?😴"]
DONATING_ENOUGH = ["(S)He must be a good person! 😽"]
DONATING_MORE_THAN_ENOUGH = ["Do you owe him lots of money or what? 😹"]
