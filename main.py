from pydub import AudioSegment
import os, time, glob, datetime
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


BOT_TOKEN = " "
API_ID = " "
API_HASH = " "

bot = Client(
    ":memory:",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

refresh_button = [
    InlineKeyboardButton(
        text='Refresh List',
        callback_data='refresh'
    )
]
dir = os.getcwd().replace('\\', '/') + '/'
vdir = 'C:/Users/Administrator/Downloads/Telegram Desktop/*'
a1 = dir + '1.mp3'
a2 = dir + '2.mp3'
a3 = dir + '3.mp3'
a6 = dir + '6.mp3'
aac = dir + 'a.aac'
msgid = 0
chatid = 0
@Bot.on_message(filters.text)
async def start(bot, m):
    keyboard = []
    keyboard.append(refresh_button)
    try:
        for file in glob.glob(vdir):
            keyboard.append(
                [
                    InlineKeyboardButton(
                        text=file.rsplit('/', 1)[1].replace('Telegram Desktop\\', ''),
                        callback_data=file.rsplit('/', 1)[1].replace('Telegram Desktop\\', '')
                    )
                ]
            )
    except Exception as e:
        print(e)
        return
    keyboard.append(refresh_button)
    #await bot.send_message(chat_id=id, text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
    await m.reply_text(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))


@bot.on_callback_query()
async def callback(bot, update):
    global chatid
    global msgid
    if update.data == "refresh":
        keyboard = []
        keyboard.append(refresh_button)
        try:
            for file in glob.glob(vdir):
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            text=file.rsplit('/', 1)[1].replace('Telegram Desktop\\', ''),
                            callback_data=file.rsplit('/', 1)[1].replace('Telegram Desktop\\', '')
                        )
                    ]
                )
        except Exception as e:
            print(e)
            return
        keyboard.append(refresh_button)
        await update.message.edit(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    try:
        for file in glob.glob(vdir):
            if file.rsplit('/', 1)[1].replace('Telegram Desktop\\', '') == update.data:
                await update.message.reply_text('downloading..')
                vname = file.rsplit('/', 1)[1].replace('Telegram Desktop\\', '')
                ext = '.' + file.rsplit('.', 1)[1]
                
                v = dir + '1' + ext
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
    os.system(f'ffmpeg -i {v} -vn -i {a1} -vn -i {a2} -vn -i {a3} -vn -i {a6} -vn -filter_complex "[1]adelay=00000|00000[b]; [2]adelay={t2}|{t2}[c]; [3]adelay={t3}|{t3}[d]; [4]adelay={t6}|{t6}[e]; [0][b][c][d][e]amix=5" -c:a aac -b:a 125k -y {aac}')   
    time.sleep(10)
    out_vid = dir + vname
    os.system(f'ffmpeg -i {v} -i {aac} -c copy -map 0:0 -map 1:0 -y "{out_vid}"')
    await m.reply_video(video=out_vid, file_name=vname)
    

bot.run()
