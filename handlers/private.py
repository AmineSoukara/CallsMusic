from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    pic = "https://i.imgur.com/cCKoCHj.jpg"
    mention = f"{message.from_user.mention}"
    await message.reply_photo(pic,
        caption = f"""Hello 👋 {mention},
Nice To Meet You !, I'm MarsPyro, I Can Let You Play Music In Your Group's Voice Chat.

The Commands I Currently Support Are:

/play - Play The Replied Audio File Or YouTube Video
/pause - Pause The Audio Stream
/resume - Resume The Audio Stream
/skip - Skip The Current Audio Stream
/stop - Clear The Queue And Remove The X-Bot From The Call

**Thanks To :** PyTgCalls & C.M
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
