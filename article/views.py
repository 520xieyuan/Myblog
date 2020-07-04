from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from utils import identify
from .models import Article
import json
import datetime
from django.views.decorators.http import require_GET
import math


# Create your views here.


class ArticleAddGet(View):
    @identify.identify_cls
    def post(self, request, decode_jwt):
        data = json.loads(request.body.decode())
        userid = decode_jwt.get("userid")
        try:
            article = Article(title=data.get("title"), content=data.get("content"), user_id=userid,
                              pub_date=int(datetime.datetime.now().timestamp()))
            article.save()
            print(article)
            return JsonResponse({"article_id": article.id}, status=201)
        except:
            return HttpResponse(status=400)

    def get(self, request: HttpRequest):
        passInPage = request.GET['page']
        passInSize = request.GET['size']
        print(passInPage, passInSize)
        try:
            if int(passInSize) <= 0 or int(passInSize) > 100:
                size = 20
            else:
                size = int(passInSize)
        except:
            size = 20

        total_items = Article.objects.count()
        total_pages = math.ceil(Article.objects.count() / size)

        try:
            if int(passInPage) <= 0:
                page = 1
            elif int(passInPage) > total_pages:
                page = total_pages
            else:
                page = int(passInPage)
        except:
            page = 1

        start = (page - 1) * size
        res = [{"article_id": art.id, "title": art.title, "pub_date": art.pub_date, "username": art.user.username}
         for art in Article.objects.filter().order_by("-pub_date")[start:start+size]]

        print(res)
        return JsonResponse({"articles": res, "pagination": {"page": page, "total_pages": total_pages,
                                                            "size": size, "total_items": total_items}}, status=202)


# 详情
@require_GET
def article_detail(request: HttpRequest, article_id):
    print(article_id)
    article = Article.objects.filter(pk=article_id).first()
    if article:
        return JsonResponse({"title": article.title, "content": article.content, "datetime": article.pub_date,
                             "username": article.user.username})
    return HttpResponse(status=400)
