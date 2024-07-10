from django.views import View
from django.shortcuts import render, redirect
from .models import TelegramUsers
from django.http import JsonResponse

from server.const import BOT_NAME
from server.const import HOST_DNS

class Main(View):
    def get(self, request):
        bot_name = BOT_NAME
        print(BOT_NAME)
        session_id = request.session["session_id"]
        auth = request.session["auth"]
        return render(request, 'main.html', {"bot_name":bot_name, "session_id":session_id, "auth":auth, "dns":HOST_DNS})
    
class Login(View):
    def get(self, request):
        session_id = request.session["session_id"]
        telegram_login_url = f"https://t.me/{BOT_NAME}?start={session_id}"
        return redirect(telegram_login_url)

class AuthCheck(View):
    def get(self, request):
        session_id = request.GET.get('session_id')
        if TelegramUsers.objects.filter(session_id=session_id).exists():
            return JsonResponse({'result': True})
        else:
            return JsonResponse({'result': False})

class Logout(View):
    def get(self, request):
        session_id = request.session["session_id"]
        if TelegramUsers.objects.filter(session_id=session_id).exists():
            user = TelegramUsers.objects.get(session_id=session_id)
            user.session_id = "None"
            user.save()

        request.session["session_id"]=None
        request.session["auth"]=None
        request.session["name"]=None
        request.session["org_select"]=None
        return redirect("/")