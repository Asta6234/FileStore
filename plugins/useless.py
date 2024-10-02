from bot import Bot
from pyrogram.types import Message
from pyrogram import filters, enums
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)


@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        await message.reply_text(
            f"<b>ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ ɪs:</b> <code>{user_id}</code>", quote=True
        )
