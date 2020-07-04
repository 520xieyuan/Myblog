from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.http import require_POST
from .models import User
import bcrypt
import json
import jwt
import datetime
from myblog.settings import SECRET_KEY
from utils import identify
from .tasks import sendemail
from django.db import transaction

# Create your views here.

EXPIRE_TIME = 60 * 60


@require_POST
def login(request: HttpRequest):
    # try:
    data = json.loads(request.body.decode())
    email = data.get("email")
    user = User.objects.filter(email=email).first()
    print(user)
    if not user:
        return HttpResponse(status=400)
    else:
        if bcrypt.checkpw(data.get("password").encode(), user.password.encode()):
            payload = {"userid": user.id, "exp": int(datetime.datetime.now().timestamp()) + EXPIRE_TIME}
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode()
            print(token)

            return JsonResponse({"token": token})
        else:
            return HttpResponse(status=400)


# except:
#     return JsonResponse({"test": 123}, status=400)


@require_POST
def reg(request: HttpRequest):
    data = json.loads(request.body.decode())
    try:
        email = data.get("email")

        if User.objects.filter(email=email).first():
            return JsonResponse({"error": "user has existed"}, status=400)
        else:
            password = data.get("password")
            new_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            username = data.get("username")
            user = User(email=email, username=username, password=new_password.decode())
            with transaction.atomic():
                user.save()
                # 异步任务
                sendemail.delay()

            return JsonResponse({"res": "success"})
    except:
        return JsonResponse({"why": 123}, status=400)


@identify.identify
def checktoken(request: HttpRequest):
    return HttpResponse()


def test(request):
    return HttpResponse("<h1>hello</h1>")

