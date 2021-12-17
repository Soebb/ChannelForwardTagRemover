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

invoice = "12345"
@bot.on_message(filters.text)
async def startt(bot, m):
    global invoice
    if 'check' in m.text:
        url = 'https://poolam.ir/invoice/check/' + invoice
        params = {"api_key":poolam_api_key}
        r = requests.post(url, data=params)
        if r.json()['status'] == 1:
            await m.reply(return_link)
        else:
            await m.reply('پرداختی صورت نگرفته است\n\nدرصورت بروز خطا به آیدی زیر پیام بدید\n@mrmacvin')
    else:
        url = 'https://poolam.ir/invoice/request'
        params = {"api_key":poolam_api_key, "amount":int(Price_rial), "return_url":urllib.parse.quote('http://zil.ink/dlmacvin')}
        r = requests.post(url, data=params)
        invoice = f"{r.json()['invoice_key']}"
        await m.reply("https://poolam.ir/invoice/pay/" + invoice)


bot.run()
