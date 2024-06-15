from dataclasses import dataclass, field
import requests, json
from server.const import TOKEN_TG

@dataclass
class Message:
    chat_id : str = None
    message_id : str = None
    username : str = None
    last_name : str = None
    first_name : str = None
    text : str = None
    photo : str = None
    voice : str = None
    video_note : str = None
    video : str = None
    document : str = None
    callback : str = None
    error : bool = field(init=False)

    def __post_init__(self):
        if not self.chat_id  or not self.message_id:
            self.error = True
        else:
            self.error = False

    def sendMessage(self, keyboard={}, text="text"):

        data = { 
            "chat_id": self.chat_id,
            "text": text,
            "reply_markup" : json.dumps(keyboard)
        }
        response = requests.post(f"https://api.telegram.org/bot{TOKEN_TG}/sendMessage", data)
        return response
    

    def editMessage(self, text=" ", message_id=None, keyboard={}):
        if not message_id:
            message_id = self.message_id

        data = { 
            "chat_id": self.chat_id,
            "text": text,
            "message_id" : message_id,
            "reply_markup" : json.dumps(keyboard)
        }
        response = requests.post(f"https://api.telegram.org/bot{TOKEN_TG}/editMessageText", data)
        return response

    def deleteMessage(self, message_id=None):
        if not message_id:
            message_id = self.message_id

        data = {
            "chat_id": self.chat_id,
            "message_id" : message_id
        }
        response = requests.post(f"https://api.telegram.org/bot{TOKEN_TG}/deleteMessage", data)
        return response
    
        
    def callbackJson(self):
        try:
            callback_json = json.loads(self.callback)  
        except:
            callback_json = None
        return callback_json