from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6490244951"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/fd2d1b9bdef248cd900f9.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/e6bd1a3f1fe9a62328b07.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GOVIND_USERBOT_SPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GOVIND_USERBOT_UPDATE")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6540170882").split()))


FAILED = "https://te.legra.ph/file/9f62f4091405b8476b379.jpg"
