from django.shortcuts import redirect
import secrets
from .models import TelegramUsers
from django.utils import timezone

class CheckSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "bot" in request.path or "auth_check" in request.path:
            print("")
            print("SessionMiddll ignore /bot or /auth")
            print("")
            response = self.get_response(request)
            return response

        if "session_id" in request.session and TelegramUsers.objects.filter(session_id=request.session["session_id"]).exists():
            user = TelegramUsers.objects.get(session_id=request.session["session_id"])
            request.session["auth"] = True
            request.session["name"] = user.name
            
        else:
            session_id = secrets.token_hex(16)
            while TelegramUsers.objects.filter(session_id=session_id).exists():
                session_id = secrets.token_hex(16)
            request.session["session_id"] = session_id
            request.session["auth"] = None
            request.session["name"] = None


        response = self.get_response(request)
        return response
    

class SessionDebuger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "bot" in request.path or "auth_check" in request.path:
            print("")
            print("SessionDebbugerMidd ignore /bot in request.path")
            print("")
            response = self.get_response(request)
            return response
        
        session_id = request.session["session_id"]
        auth = request.session["auth"]
        name = request.session["name"]


        print("##_______SESSION____##")
        print(f"session_id - {session_id}")
        print(f"auth       - {auth}")
        print(f"name       - {name}")
        print(" ")
        print(" ")

        path_exceptions = [
            "/",
            "/bot",
            "/login/",
            "/logout/",
            "/auth_check/",
        ]

        if request.path in path_exceptions or request.session["auth"] or "/admin" in request.path:
            response = self.get_response(request)
            return response
        
        else:
            print(" ")
            print("##_______REDIRECT____##")
            print(f"SessionDebugerMidd redirect {request.path} to the /")
            print("exception path")
            print("")
            print("")
            return redirect("/")