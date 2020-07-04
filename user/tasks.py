from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from myblog.celery import app
from celery import shared_task
import time


@shared_task
def sendemail():
    send_mail(
        'Subject here',
        'Here is the message.',
        'magetest@magedu.com',
        ['1291063254@qq.com'],
        fail_silently=False,
        html_message="<h1>lala</h1>",
    )
    print("++++++++++++")


