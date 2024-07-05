from .models import Message

def telegram_format(request):
    r = flatten_json(request)
    # print(r)

    # MAIN
    if "message.from.id" in r:
        chat_id = str(r["message.chat.id"])
    elif "callback_query.message.chat.id" in r:
        chat_id = str(r["callback_query.message.chat.id"])
    else:
        chat_id = None

    if "message.message_id" in r:
        message_id = str(r["message.message_id"])
    elif "callback_query.message.message_id" in r:
        message_id = str(r["callback_query.message.message_id"])
    else:
        message_id = None

    # USER META
    if "message.from.username" in r:
        username = r["message.from.username"]
    elif "callback_query.message.chat.username" in r:
        username = r["callback_query.message.chat.username"]
    else:
        username = None

    if "message.from.first_name" in r:
        first_name = r["message.from.first_name"]
    elif "callback_query.message.chat.first_name" in r:
        first_name = r["callback_query.message.chat.first_name"]
    else:
        first_name = None

    if "message.from.last_name" in r:
        last_name = r["message.from.last_name"]
    elif "callback_query.message.chat.last_name" in r:
        last_name = r["callback_query.message.chat.last_name"]
    else:
        last_name = None
    
    # CONTENT META
    if "message.text" in r:
        text = r["message.text"]
    else:
        text = None

    if "message.photo" in r:
        photo = r["message.photo"][0]["file_id"]
    else:
        photo = None
    
    if "message.voice.file_id" in r:
        voice = r["message.voice.file_id"]
    else:
        voice = None
    
    if "message.video_note.thumbnail.file_id" in r:
        video_note = r["message.video_note.thumbnail.file_id"]
    else:
        video_note = None
    
    if "message.video.thumbnail.file_id" in r:
        video = r["message.video.thumbnail.file_id"]
    else:
        video = None

    if "message.document.file_id" in r:
        document =  r["message.document.file_id"]
    else:
        document = None
    
    if "callback_query.data" in r:
        callback = r["callback_query.data"]
    else:
        callback = None

    message = Message(
        chat_id=chat_id,
        message_id=message_id,
        username=username,
        last_name=last_name,
        first_name=first_name,
        text=text,
        photo=photo,
        voice=voice,
        video=video,
        document=document,
        callback=callback
    )
    return message


def flatten_json(json_obj, prefix=''):
    flat_json = {}
    for key, value in json_obj.items():
        new_key = f"{prefix}{key}"
        if isinstance(value, dict):
            flat_json.update(flatten_json(value, f"{new_key}."))
        else:
            flat_json[new_key] = value
    return flat_json
