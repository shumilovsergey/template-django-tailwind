from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

# t.me/sh_login_testing_bot
TOKEN_TG = os.getenv("TOKEN_TG")
HOST_DNS = os.getenv("HOST_DNS")
BOT_NAME = os.getenv("BOT_NAME")
PORT = os.getenv("PORT")
#HARDCODE

#BUTTONS

BACK_BUTTON= {
    "inline_keyboard" :  [
        [
            {'text': 'Вернуться на сайт', 'url': f"https://{HOST_DNS}/"}      
        ]
    ]
}

CLEAN_BUTTON= {
    "inline_keyboard" :  [
        [
            {'text': 'Вернуться на сайт', 'url': f"https://{HOST_DNS}/logout/"}      
        ]
    ]
}