import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 25529076))

    API_HASH = str(os.environ.get("API_HASH", "b8109a26ed1ba595aa5d70d0e38c3806"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1428968542))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    START = str(os.environ.get("START_TEXT", ""))

    HELP = str(os.environ.get("HELP_TEXT", ""))

    DONATE = str(os.environ.get("DONATE_TEXT", ""))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/HeimanSupports"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/HeimanSupport"))

    DB_URL = str(os.environ.get("DB_URL", ""))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedback_bot"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))

