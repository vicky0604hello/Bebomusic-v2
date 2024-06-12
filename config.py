from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "15668511"))
API_HASH = getenv("API_HASH", "3dca0a7ecbf79c58c06d4e96845833f9")

BOT_TOKEN = getenv("BOT_TOKEN", "6756167396:AAGMYggl3TEJWDWArVTwSgMBlc6euOVdiUU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5350640981"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/fd2d1b9bdef248cd900f9.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/e6bd1a3f1fe9a62328b07.jpg")

SESSION = getenv("SESSION", "BQF1_JUAxBX4oZ58NYiyDGH7_OyJyECCtWpiml_ppUmJwjpQ_OWQC6YfCIKH1Y2VZN5LaubODmPU_FfXB2ehku_MsU9rCSJluuB0dAnNGbVE8hYWAcLr2PL-EpDqeSVHkb92q2gKQh-6YrAOrGYG4ZmrjqE6xaey36TZnF9U_OemDhOFmSxt0M913TWfX35Obkr2XsuGP83B4m5BcY84quLyGmNhDH-X4cOLIz2NGjn5_AHZngisxeHSBvulfyewss0uL_15AT8G2NAcBvX_fjS2FCXKC4X8UfKgzpuLew2pRTboxu2rw6BNjxKjTJh6nZ1bP703_2Y__5IgxaHsqBjAZF1QiQAAAAFaa_39AA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/botverse_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GOVIND_USERBOT_UPDATE")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6540170882").split()))


FAILED = "https://te.legra.ph/file/9f62f4091405b8476b379.jpg"
