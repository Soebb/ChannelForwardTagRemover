from pydub import AudioSegment
import os, json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  
import urllib.parse


BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

bot = Client(
    "poolam",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

@bot.on_message(filters.audio)
async def startt(bot, m):
    await m.download('a.mp3')
    song = AudioSegment.from_mp3("a.mp3")
    end = AudioSegment.from_mp3("b.mp3")
    with = song.append(end, crossfade=1500)
    with.export('m.mp3')
    await m.reply_audio(audio='m.mp3')


bot.run()





