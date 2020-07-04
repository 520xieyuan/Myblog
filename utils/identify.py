import json
import jwt
from django.http import HttpResponse, HttpRequest
from django.conf import settings


def identify(obj):
    def wrapper(request: HttpRequest, *args, **kwargs):
        print(request.META.get("HTTP_TOKEN"))
        data = json.loads(request.body.decode())
        user_jwt = data.get('token')
        try:
            jwt.decode(user_jwt, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return HttpResponse(status=400)

        return obj(request, *args, **kwargs)

    return wrapper


def identify_cls(func):
    def wrapper(instance, request, *args, **kwargs):
        print(request.META.get("HTTP_TOKEN"))
        data = json.loads(request.body.decode())
        user_jwt = data.get('token')
        try:
            print(111111, user_jwt)
            decode_jwt = jwt.decode(request.META.get("HTTP_TOKEN").encode(), settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return HttpResponse(status=410)

        return func(instance, request, decode_jwt,*args, **kwargs)

    return wrapper
