from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, 'base.html', {'base_dir': settings.BASE_DIR} )


# def today_is(request):
#     now = datetime.datetime.now()
#     return render(request, 'blog/blog-article-old.html',
#                   {'now': now, 'main_nav': 'includes/nav.html', 'base_dir': settings.BASE_DIR})
