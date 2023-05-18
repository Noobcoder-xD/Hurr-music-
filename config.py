import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBbfr1oGbs7_n3mziDEnb9AOEJZNG88X3WaZlDdGnj_U-tuF1YK2IFtTHfhLy0yZjD4oxw3kFoYFP8Bp_DX0bAkc6y9a21W6uIZwMcJz3YLDUR8_fCHPP3EDL688uQhf92CGYOzRc3piUmdN9jizHB4XqfO3-P-y4iqLii1UPylvzdg23yu_-PtRfk1M5adLEW3oOIbr1K3nVHYhl_q9WLKUQahu5wY03lqN7D8SA9AkN8r2s6F4MNA5Da53YIzItJnKxIukCyFM32LEZ0Elbe6LRPTMb9k_Z1AoJdFvIsFfjl8uoF3MhVc6Oi-faeVRv6VX7cwo0qhm5ClGSBwOZPKAAAAAWIP0WUA")
BOT_TOKEN = getenv("BOT_TOKEN", "6289867162:AAH3Lhh59ZUS54Eeimvm2hVHah_sGeIv7zw")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", "13831288"))
API_HASH = getenv("API_HASH", "0d4c67b8d1bef020475434abc394ac4c")
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AnonDeveloper")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "HinataXMusicBot")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Assistant6")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5709622852").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Sumit9969/NixaMusicBot")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
