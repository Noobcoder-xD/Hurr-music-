import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQALcBcEcDiQ5WD3D-lzhrs3iJA48O0lIKGYdIwGeXIeTR292X3L8mKm6VMGIzMMLkuV13uzaNnqav-sxvhmcnlUU_dnJFNV7tVn8Jlb9mr5zKCIrx5z7LF9_8LAM96ZhzYnRbNPhAB8KOKCSlZZjSuqLFonIPQB_AZTzmyNCzBRD7CMeI4ZUe38BbWogG1WZ6XRn2c1UGYNAff5CekMXwDJ1RteM01OGwoXyyPGIjgJdZGVB-TqfyR-9opwtwQOA8WBBMSMaAG1AasEiuzcy46tFItTLvfMXJ5_bAGub0AqSwz5fD01pT8Os7-MGU_-xkLTATmNXk22NkBLDuW73mCnAAAAAaSw7BgA")
BOT_TOKEN = getenv("BOT_TOKEN", "6935496455:AAGndnOEhoNwWrtMzfGCEipdIQruucVVWdg")
BOT_NAME = getenv("BOT_NAME", "testing")
API_ID = int(getenv("API_ID", "28037022"))
API_HASH = getenv("API_HASH", "ef7435f8daa6bfe1611eb01f7e0a4778")
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TG_MOVIEZ_KING")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "jsjjwjsjjsjsnsnsnnsnsbot")
OWNER_ID = getenv("OWNER_ID", "6903041211")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Hsjsjsjjsjsjsjjsgsg")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TeleBotxSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TeleBotsUpdate")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5709622852").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/LoveFeelingsWill/Hurr-music-")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
