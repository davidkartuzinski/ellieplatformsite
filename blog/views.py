from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.conf import settings


def post_list(request):
    return render(request, 'blog/post_list.html', {'base_dir': settings.BASE_DIR})
    # return render(request, 'base.html', {'base_dir': settings.BASE_DIR})


print(settings.BASE_DIR, "boo")
# def today_is(request):
#     now = datetime.datetime.now()
#     return render(request, 'blog/blog-article-old.html',
#                   {'now': now, 'main_nav': 'includes/nav.html', 'base_dir': settings.BASE_DIR})
