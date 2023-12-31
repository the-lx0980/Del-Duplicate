import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = 6353248

    # Get from my.telegram.org
    API_HASH = '1346f958b9d917f0961f3e935329eeee'

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
