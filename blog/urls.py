from django.conf.urls import url
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('<slug:slug>/', views.blog_post, ),
    path('<slug:slug>/', views.blog_post, name="blog_post"),
    # name='blog_post'),
    path('author', views.author_post_list, name='author_post_list'),
    path('category/<slug:slug>/', views.category, name='category'),
]
