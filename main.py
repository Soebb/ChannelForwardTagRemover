import os, json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  
import urllib.parse


bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@bot.on_message(filters.text)
async def startt(bot, m):
    #headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'https://poolam.ir/invoice/request'
    params = {"api_key":"dd82f80e2c0746c16a975884a73b73b5", "amount":10000, "return_url":urllib.parse.quote("http://tarafdari.com/node/2043656")}
    r = requests.post(url, data=params)
    print(r.json()['invoice_key'])


bot.run()
