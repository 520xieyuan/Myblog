from django.conf.urls import url
from .views import login, reg, checktoken, test

urlpatterns = [
    url('^login$', login),
    url('^reg$', reg),
    url('^token$', checktoken),
    url('^test$', test),
]