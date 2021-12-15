import os, json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  



bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@bot.on_message(filters.text)
async def startt(bot m):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(m.text, data=params, headers=headers)
    print(r.json())
