'''import os
import time
from datetime import datetime

import psutil
from pyrogram import Client, filters
from pyrogram.types import Message

from Yukki import BOT_USERNAME, MUSIC_BOT_NAME, app, boottime
from Yukki.Utilities.ping import get_readable_time

__MODULE__ = "Ping"
__HELP__ = """

/ping - Check if Bot is alive or not.
"""


async def bot_sys_stats():
    bot_uptime = int(time.time() - boottime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
Uptime: {get_readable_time((bot_uptime))}
CPU: {cpu}%
RAM: {mem}%
Disk: {disk}%"""
    return stats


@app.on_message(filters.command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    start = datetime.now()
    response = await message.reply_photo(
        photo="https://telegra.ph/file/3b583788e713096b24e2e.png",
        caption=">> 𝗣𝗢𝗡𝗚!",
    )
    uptime = await bot_sys_stats()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(
        f"**𝗣𝗢𝗡𝗚!!**\n`⚡{resp} ms`\n\n<b><u>{MUSIC_BOT_NAME} 𝗠𝗢𝗜 𝗦𝗧𝗔𝗧𝗘𝗦🔁:</u></b>{uptime}"
    )
'''
