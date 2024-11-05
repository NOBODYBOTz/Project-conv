import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 25529076))

    API_HASH = str(os.environ.get("API_HASH", "b8109a26ed1ba595aa5d70d0e38c3806"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1715861188))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1715861188").split())

    START = str(os.environ.get("START_TEXT", "hello this is welcome massage for testing.."))

    HELP = str(os.environ.get("HELP_TEXT", "it's testing time so no help.!"))

    DONATE = str(os.environ.get("DONATE_TEXT", ""))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/NOBODYBOTz"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/NOBODYBOTz"))

    DB_URL = str(os.environ.get("DB_URL", "mongodb+srv://avinashkakde646:avinashkakde646@cluster0.jlubkn6.mongodb.net/?retryWrites=true&w=majority"))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedback_bot"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001955617973"))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))

