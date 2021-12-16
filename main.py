import os, json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  
import urllib.parse


BOT_TOKEN = " "
API_ID = " "
API_HASH = " "
poolam_api_key = " "
Price_rial = "100000"
return_link = "http://cptid.ml/stplay/6TL4"


bot = Client(
    "poolam",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

@bot.on_message(filters.text)
async def startt(bot, m):
    url = 'https://poolam.ir/invoice/request'
    params = {"api_key":poolam_api_key, "amount":int(Price_rial), "return_url":urllib.parse.quote(return_link)}
    r = requests.post(url, data=params)
    await m.reply(f"https://poolam.ir/invoice/pay/{r.json()['invoice_key']}")


bot.run()
