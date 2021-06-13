"""elliesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views as staticviews

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, FlatPageSitemap

from . import views

sitemaps = {
    'posts': PostSitemap,
    'flatpages': FlatPageSitemap,
}

# https://overiq.com/django-1-10/handling-media-files-in-django/
regular_patterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
flatpage_patterns = [
    # https://docs.djangoproject.com/en/3.2/ref/contrib/flatpages/#using-the-urlconf

    # example path('privacy-policy/', staticviews.flatpage, {'url': '/privacy-policy/'}, name='privacy-policy'),
    path('', staticviews.flatpage, {'url': '/home/'}, name='home'),
    path('home/', views.index, name='index'),
    re_path(r'^(?P<url>.*/)$', staticviews.flatpage),
]

media_root = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_root = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = regular_patterns + media_root + static_root + flatpage_patterns
