from django.conf.urls import url
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # url(r'^$', views.post_list, name='post_list'),
]
