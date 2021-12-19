from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2, command
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME, UPDATES_CHANNEL, GROUP_SUPPORT


@Client.on_message(command(["start"]) & other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**اهلا انا بوت اسمي {bn}
استطيع تشغيل الاصوات في المحادثة الصوتية الخاصة بمجموعتك
يمكنك اضافتي الي المجموعة و تشغيل الموسيقي و الاستمتاع**""",
        reply_markup=InlineKeyboardMarkup(
            [
               [
                    InlineKeyboardButton(
                        "『𝑴𝑺』𝑺𝑨𝑴𝑬𝑬𝑹 📿",
                        url="https://t.me/s_000m",
                    )
                ],[
                    InlineKeyboardButton(
                       "جروب الدعم 💬", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "قناة لتحديثات", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],[
                    InlineKeyboardButton(
                        "اضف البوت الي مجموعتك",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        )
    )
