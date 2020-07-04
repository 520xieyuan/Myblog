from django.conf.urls import url
from .views import ArticleAddGet, article_detail

urlpatterns = [
    url("^$", ArticleAddGet.as_view()),
    url(r'^(\d*)$', article_detail),
]