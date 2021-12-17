from pydub import AudioSegment
import os, json
from pyromod import listen
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

@bot.on_message(filters.video | filters.document)
async def startt(bot, m):
    await m.reply('downloading..')
    vid = m.video or m.document
    vname = vid.file_name
    await m.download(os.path.join(os.getcwd(), f'v.{vid.file_name.rsplit(".", 1)[1]}'))
    aud = await bot.ask(m.chat.id,'صوت 2.1 رو بفرست', filters=filters.audio)
    await bot.download_media(message=aud.audio, file_name=os.path.join(os.getcwd(), '2.1.mp3'))
    t2 = await bot.ask(m.chat.id,'تایم صوت 2 (2.2 + 2.1) رو بفرست', filters=filters.text)
    t3 = await bot.ask(m.chat.id,'تایم صوت 3 رو بفرست\n3.mp3', filters=filters.text)
    t6 = await bot.ask(m.chat.id,'تایم صوت 6 رو بفرست\n6.mp3', filters=filters.text)
    a2_1 = AudioSegment.from_mp3(os.path.join(os.getcwd(), '2.1.mp3'))
    a2_2 = AudioSegment.from_mp3(os.path.join(os.getcwd(), '2.2.mp3'))
    aa2 = a2_1.append(a2_2)
    aa2.export("2.mp3", format="mp3")
    a2 = os.path.join(os.getcwd(), '2.mp3')
    a3 = os.path.join(os.getcwd(), '3.mp3')
    a6 = os.path.join(os.getcwd(), '6.mp3')

    song = AudioSegment.from_mp3(os.path.join(os.getcwd(), 'a.mp3'))

    end = AudioSegment.from_mp3("b.mp3")
    #wit = song.append(end)
    wit = song.append(end, crossfade=1500)
    wi = wit + song
    wi.export("m.mp3", format="mp3", bitrate="192k")
    await m.reply_audio(audio='m.mp3')


bot.run()





