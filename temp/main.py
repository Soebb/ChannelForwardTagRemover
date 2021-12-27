from pydub import AudioSegment
import os, time, glob, datetime
import PTN
import shutil
from telethon import TelegramClient, events


BOT_TOKEN = " "
API_ID = "6"
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

Bot = TelegramClient("Bot", int(API_ID), API_HASH).start(bot_token=BOT_TOKEN)


folder = 'C:/Users/Administrator/Downloads/Telegram Desktop'

msgid = 0
chatid = 0
vdir = folder + '/*'
dir = 'C:/voicetag/'
a1 = dir + '1.mp3'
a2 = dir + '2.mp3'
a3 = dir + '3.mp3'
a6 = dir + '6.mp3'
aac = dir + 'a.aac'
org = dir + 'org.mp3'
main = folder.rsplit('/', 1)[1] + '\\'

def gettime(t2):
    try:
        tt2 = t2.split('.')[1]
        t2 = t2.split('.')[0]
        t2 = f'0{t2[:1]}:{t2[:3][1:]}:{t2[3:]}'
    except:
        tt2 = None
        t2 = f'0{t2[:1]}:{t2[:3][1:]}:{t2[3:]}'
    t2 = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(t2.split(":"))))
    if tt2 != None:
        t2 = f'{t2}{tt2[:1]}00'
    else:
        t2 = f'{t2}000'
    return t2

@Bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def expor(event):
    if event.text and event.text.startswith("/"):
        await event.reply("ورودی رو بفرست")
        return
    await event.reply("processing..")
    if not os.path.isdir('temp/'):
        os.makedirs('temp/')
    #media = m.audio or m.video or m.document
    vname = event.file_name
    file = 'temp/input.mp3'
    try:
        #await m.reply("downloading..")
        if vname.rsplit('.', 1)[1].lower() == "mp3":
            await Bot.download_media(event.media, file)
        else:
            fil = await Bot.download_media(event.media, 'temp/')
            os.system(f'ffmpeg -i "{fil}" -vn -y {file}')

        #file = 'temp/input.mp3'
        #await m.download(file)
        ext = '.' + file.rsplit('.', 1)[1]
        #v = folder + '/' + vname
        #vname = vname.replace('.ts', '.mp4')
        try:
            os.remove(a2)
        except:
            pass
        try:
            os.remove(dir + '2.1.mp3')
        except:
            pass
        try:
            os.remove('temp/mix.mp3')
        except:
            pass
        n = PTN.parse(vname)
        title = n['title'].replace("-", " ")
        au2_1 = f'C:/All Projact Primer Pro/Audio Sound Serial Primer Pro Tag/{title}/2.1.mp3'
        shutil.copyfile(au2_1, dir + '2.1.mp3')
        #askaud = await m.reply_text('صوت 2.1 رو بفرست تا با 2.2 ادغام کنم')
        #aud: Message = await bot.listen(m.chat.id, filters=filters.audio)
        #await bot.download_media(message=aud.audio, file_name=dir + '2.1.mp3')
        async with Bot.conversation(event.chat_id) as conv:
            await conv.send_message('تایم صوت 2 بفرست')
            response = await conv.get_response()
            time2 = response.text
            await conv.send_message('پنج تا تایم باهم بفرست واسه تگ سوم')
            respons = await conv.get_response()
            time3 = respons.text
            await conv.send_message('تایم صوت 6 بفرست')
            respon = await conv.get_response()
            time6 = respon.text
        t2 = int(gettime(time2))
        t3_1, t3_2, t3_3, t3_4, t3_5 = time3.split()
        t3_1 = int(gettime(t3_1))
        t3_2 = int(gettime(t3_2))
        t3_3 = int(gettime(t3_3))
        t3_4 = int(gettime(t3_4))
        t3_5 = int(gettime(t3_5))
        t6 = int(gettime(time6))
        #processmsg = await update.message.reply_text('processing..')
        a2_1 = AudioSegment.from_mp3(dir + '2.1.mp3')
        a2_2 = AudioSegment.from_mp3(dir + '2.2.mp3')
        aa2 = a2_1.append(a2_2)
        aa2.export(dir+"2.mp3", format="mp3")
        #os.system(f'ffmpeg -i "{file}" -vn -y org.mp3')
        aud2 = AudioSegment.from_mp3(a2)
        aud3 = AudioSegment.from_mp3(a3)
        audorg = AudioSegment.from_mp3(file)
        aud1 = AudioSegment.from_mp3(a1)
        aud6 = AudioSegment.from_mp3(a6)
        out = audorg.overlay(aud1, gain_during_overlay=-2)
        out = out.overlay(aud2, position=t2, gain_during_overlay=-2)
        out = out.overlay(aud3, position=t3_1, gain_during_overlay=-2)
        out = out.overlay(aud3, position=t3_2, gain_during_overlay=-2)
        out = out.overlay(aud3, position=t3_3, gain_during_overlay=-2)
        out = out.overlay(aud3, position=t3_4, gain_during_overlay=-2)
        out = out.overlay(aud3, position=t3_5, gain_during_overlay=-2)
        out = out.overlay(aud6, position=t6, gain_during_overlay=-2)
        out.export("temp/mix.mp3", format="mp3")
        #os.system(f'ffmpeg -i mix.mp3 -y a.aac')
        time.sleep(10)
        # os.system(f'ffmpeg -i "{file}" -i a.aac -c copy -map 0:0 -map 1:0 -y "{vname}"')
        #await m.reply_audio(audio='temp/mix.mp3')
        await Bot.send_file(event.chat_id, file='temp/mix.mp3')
        try:
            os.remove(file)
        except:
            pass
    except Exception as e:
        print(e)



Bot.run_until_disconnected()
