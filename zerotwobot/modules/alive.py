import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO ="https://telegra.ph/file/6fa5f235ded76e554249b.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Luffy. The Sun God.** \n\n"
  TEXT += "❍ **I'm Working Properly** \n\n"
  TEXT += f"❍ **My Master : [Axel](https://t.me/YuitoSan)** \n\n"
  TEXT += f"❍ **Library Version :** `{telever}` \n\n"
  TEXT += f"❍ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"❍ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✉️", "https://t.me/https://t.me/NikaSupportChat"), Button.url("Chat Group 📡", "https://t.me/animeuniversediscusion")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
