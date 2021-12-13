import os
import html5lib
import cloudscraper
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  
from bs4 import BeautifulSoup


bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

scraper = cloudscraper.create_scraper()



T = '24' + ' ya el'

@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply(f'س {T} خ')


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(c, m):
    headers = {
        "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    URL = f'{m.text}'
    r = scraper.get(URL, headers=headers)
    print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.findAll('a')
    li = soup.findAll('p')
    print(links)
    print(li)
    for link in links:
        result = link['href']
        print(f"{result}")
        await m.reply(f"{result}")
            
    


bot.run()
