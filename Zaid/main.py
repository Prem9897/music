import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import BOT_TOKEN as TOKEN



bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins={"root": "Zaid.Player"},
)

Test = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

call_py = PyTgCalls(Test)
