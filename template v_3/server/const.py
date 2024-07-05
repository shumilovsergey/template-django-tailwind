from dotenv import load_dotenv
import os

load_dotenv()

# t.me/sh_login_testing_bot
TOKEN_TG = os.getenv("TOKEN_TG")
HOST_DNS = os.getenv("HOST_DNS")
BOT_NAME = os.getenv("BOT_NAME")
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