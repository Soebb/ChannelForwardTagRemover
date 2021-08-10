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



START_TXT = """
Hi {}, I'm Forward Tag Remover bot.\n\nForward me some messages, i will remove forward tag from them.\nAlso can do it in channels.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/ChannelForwardTagRemover'),
        ]]
    )


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(c, m):
    headers = {
        "User-agent": 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}
    URL = 'https://worldsubtitle.site/movies/a-savage-nature-2020'
    try:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll('a')
        li = soup.findAll('p')
        print(links)
        print(li)
        for link in links:
            link_url = link["href"]
            print(link_url)
            await m.reply(f"{link_url}")
    except Exception as e:
        print(e)

    


bot.run()
