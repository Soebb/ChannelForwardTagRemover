from pydub import AudioSegment
import os, time
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = " "
API_ID = " "
API_HASH = " "

bot = Client(
    "voice-tag",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

@bot.on_message(filters.video | filters.document)
async def startt(bot, m):
    dir = os.getcwd().replace('\\', '/') + '/'
    await m.reply('downloading..')
    vid = m.video or m.document
    vname = vid.file_name
    ext = '.' + vname.rsplit(".", 1)[1]
    v = dir + '1' + ext
    a0 = dir + '0.mp3'
    a1 = dir + '1.mp3'
    a2 = dir + '2.mp3'
    a3 = dir + '3.mp3'
    a6 = dir + '6.mp3'
    aac = dir + 'a.aac'
    try:
        os.remove(v)
    except:
        pass
    try:
        os.remove(a2)
    except:
        pass
    try:
        os.remove(dir + '2.1.mp3')
    except:
        pass

    await m.download(v)
    os.system(f'ffmpeg -i {v} -vn -y {a0}')
    aud = await bot.ask(m.chat.id,'صوت 2.1 رو بفرست تا با 2.2 ادغام کنم', filters=filters.audio)
    await bot.download_media(message=aud.audio, file_name=dir + '2.1.mp3')
    t2 = await bot.ask(m.chat.id,'تایم صوت 2 (2.2 + 2.1) رو بفرست', filters=filters.text)
    t3 = await bot.ask(m.chat.id,'تایم صوت 3 رو بفرست\n3.mp3', filters=filters.text)
    t6 = await bot.ask(m.chat.id,'تایم صوت 6 رو بفرست\n6.mp3', filters=filters.text)
    try:
        tt2 = t2.text.split('.')[1]
        t2 = t2.text.split('.')[0]
        t2 = f'0{t2.text[:1]}:{t2.text[:3][1:]}:{t2.text[3:]}'
    except:
        tt2 = None
        t2 = f'0{t2.text[:1]}:{t2.text[:3][1:]}:{t2.text[3:]}'
    try:
        tt3 = t3.text.split('.')[1]
        t3 = t3.text.split('.')[0]
        t3 = f'0{t3.text[:1]}:{t3.text[:3][1:]}:{t3.text[3:]}'
    except:
        tt3 = None
        t3 = f'0{t3.text[:1]}:{t3.text[:3][1:]}:{t3.text[3:]}'
    try:
        tt6 = t6.text.split('.')[1]
        t6 = t6.text.split('.')[0]
        t6 = f'0{t6.text[:1]}:{t6.text[:3][1:]}:{t6.text[3:]}'
    except:
        tt6 = None
        t6 = f'0{t6.text[:1]}:{t6.text[:3][1:]}:{t6.text[3:]}'

    t2 = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(t2.split(":"))))
    t3 = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(t3.split(":"))))
    t6 = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(t6.split(":"))))
    if tt2 != None:
        t2 = t2 + tt2[:1] + "00"
    else:
        t2 = t2 + "000"
    if tt3 != None:
        t3 = t3 + tt3[:1] + "00"
    else:
        t3 = t3 + "000"
    if tt6 != None:
        t6 = t6 + tt6[:1] + "00"
    else:
        t6 = t6 + "000"

    a2_1 = AudioSegment.from_mp3(dir + '2.1.mp3')
    a2_2 = AudioSegment.from_mp3(dir + '2.2.mp3')

    aa2 = a2_1.append(a2_2)
    aa2.export(dir+"2.mp3", format="mp3")
    ad0 = AudioSegment.from_mp3(a0)
    ad1 = AudioSegment.from_mp3(a1)
    ad2 = AudioSegment.from_mp3(a2)
    ad3 = AudioSegment.from_mp3(a3)
    ad6 = AudioSegment.from_mp3(a6)

    #os.system(f'ffmpeg -i {v} -vn -i {a1} -vn -i {a2} -vn -i {a3} -vn -i {a6} -vn -filter_complex "[1]adelay=00000|00000[b]; [2]adelay={t2}|{t2}[c]; [3]adelay={t3}|{t3}[d]; [4]adelay={t6}|{t6}[e]; [0][b][c][d][e]amix=5" -c:a aac -b:a 125k -y {aac}')   
    time.sleep(10)
    out_vid = dir + vname
    os.system(f'ffmpeg -i {v} -i {aac} -c copy -map 0:0 -map 1:0 -y "{out_vid}"')
    await m.reply_video(video=out_vid, file_name=vname)
    

bot.run()





