from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import telegram_format
from api.models import TelegramUsers
from server.const import BACK_BUTTON
from server.const import CLEAN_BUTTON

@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)
    print(message)

    if message.text and "/start" in message.text and len(message.text) > 8:
        signin(message=message, request=request)
    return Response("ok", status=200)

def signin(message, request):
    tg_id = message.chat_id
    name = message.chat_id
    text=message.text
    session_id = text.replace("/start ", "")
    qr_check = False

    if "qrcode" in session_id:
        session_id = session_id.replace("qrcode", "")
        qr_check = True

    if message.first_name:
        name = message.first_name
    elif message.username:
        name = message.username


    if TelegramUsers.objects.filter(tg_id=tg_id).exists():
        user = TelegramUsers.objects.get(tg_id=tg_id)
        user.session_id = session_id
        user.save()

    elif not TelegramUsers.objects.filter(tg_id=tg_id).exists():
        user=TelegramUsers.objects.create(
            session_id=session_id,
            tg_id=tg_id,
            name=name
        )

    else:
        print("")
        print("no match session with BD")
        print("")
        return message.sendMessage(text="Что-то пошло не так, попробуйте авторизоваться еще раз!", keyboard=CLEAN_BUTTON)
    
    if qr_check:
        return message.sendMessage(text="Вход выполнен успешно!")
    else:
        return message.sendMessage(text="Вход выполнен успешно!", keyboard=BACK_BUTTON)


