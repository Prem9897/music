## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAiOCyELShHUzX-TTFDWkaSYQ1UTjZaLQ8YVCIuyQNlScl2aqaeE-ofsZhMuUwIrE0BmTWt1IgcMqb4bvCVPomcg1de1kM3hILhPpGu-wRm-mqJqS5MQwj6ptarRYS_ATCI2qKt4lMZ3Nxv9I3OgI-M2PBX-KoqivNCYjRVoTNwV-kzKTvI_Z14CCjCEkx0ouPPcX0XQQqb5057eOzSOkjfYkK1W_G3mkypkf91OzrItqTE4DsmU8NyY6QnSMZF3lSZgVl9KX9XKVMyIciQZrkmjZnoUQ4ryoL6-yFma4lb1GFjiixW3SL-orlakCDELL_cxeJln9G5lKBXxcubxpUDAAAAATDvfKMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5545963604:AAE_X2BfKonSbcxhNPMXyEH3uvUm3vM9Vdg")
BOT_NAME = getenv("BOT_NAME", "elisa")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "denvil")
OWNER_USERNAME = getenv("OWNER_USERNAME", "denvil_xdd")
ALIVE_NAME = getenv("ALIVE_NAME", "elisa")
BOT_USERNAME = getenv("BOT_USERNAME", "miselisarobot")
OWNER_ID = getenv("OWNER_ID", "5497627952")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Elisa_play")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Elisha_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "denvil_bots")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
