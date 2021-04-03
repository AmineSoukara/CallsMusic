from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.filters import command, other_filters2

@Client.on_message(command("help") & other_filters2)
async def help(_, message: Message):
    await message.reply_text("""🇺🇸 #English 
I Can Play Music In Your Voice Chat!
But How? 🤔 Follow These Steps👇

1. Add @MarsPyroBot & @MarsPyro To Your Group.

2. Give Admin Permissions To,
- Manage Voice Chats
- Add New Admins 
(For Me & My Assistant)

3. Start A Voice Chat & Send A YouTube Link Or An Audio File(mp3).

4. Then Send /play As A Reply To Link Or File.

5. BOOM! I Play It Through Your Voice Chat Within 3 Seconds.

WARNING: Please Do Not Spam Me!

Enjoy!

🇸🇦 #Arabic 
يمكنني تشغيل الموسيقى في محادثتك الصوتية!
ولكن كيف؟ 🤔 اتبع هذه الخطوات 👇

1. أضف
@MarsPyroBot & @MarsPyro
 إلى مجموعتك.

2. امنح أذونات المسؤول لـ :
- إدارة الدردشات الصوتية
- إضافة مشرفين جدد
(بالنسبة لي ومساعدي)

3. ابدأ محادثة صوتية وأرسل رابط YouTube أو ملف صوتي (mp3).

4. ثم إرسال :
/play 
كرد لرابط أو ملف.

5. بوم! تم تشغيل البث في محادثتك الصوتية في غضون 3 ثوان.
استمتع!""")
@Client.on_message(other_filters2)
async def start(_, message: Message):
    pic = "https://i.imgur.com/cCKoCHj.jpg"
    mention = f"{message.from_user.mention}"
    await message.reply_photo(pic,
        caption = f"""👋 **Hello {mention}, I'm MarsPyro, I Can Let You Play Music In Your Group's Voice Chat.**

⚙ **The Commands I Currently Support Are:**

/play - Play The Replied Audio File Or YouTube Video
/pause - Pause The Audio Stream
/resume - Resume The Audio Stream
/skip - Skip The Current Audio Stream
/stop - Clear The Queue And Remove The X-Bot From The Call

⭐ **Thanks To:** PyTgCalls & C.M
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨‍💻 Owner", url="https://t.me/AmineSoukara"
                    ),
                    InlineKeyboardButton(
                        "🆘️ Help", url="https://telegra.ph/MarsPyro-04-03"
                    )
                ]
            ]
        )
    )
