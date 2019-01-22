from telegram import Message, Update, Bot, User
from telegram.ext import Filters, MessageHandler, run_async
from tg_bot.modules.helper_funcs.extraction import extract_user_and_text
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher
from tg_bot.modules.helper_funcs.filters import CustomFilters
from tg_bot import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, STRICT_GBAN

@run_async
def spam(bot: Bot, update: Update):
    message = update.effective_message
    args = message.text.split(None, 1)[1]
    intval = str()
    args[0]+args[1]
    for x in args:
        if x.isdigit():
            intval = intval + x
        elif not x.isdigit():
            break
    spammsg = args.lstrip(intval)[1:]
    if intval.isdigit():
        if int(intval) <= 25:
            i = 0
            while i < int(intval):
                message.reply_text(spammsg)
                i += 1
        else:
            message.reply_text("Spam yourself")
    else:
        message.reply_text("Spam yourself")


__help__ = """ spam dem nubs by @rupansh
"""

SPAM_HANDLER = DisableAbleCommandHandler("spam", spam, filters=CustomFilters.sudo_filter | CustomFilters.support_filter)
dispatcher.add_handler(SPAM_HANDLER)
