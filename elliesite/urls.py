from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views as staticviews

from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps.views import index
from blog.sitemaps import PostSitemap, FlatPageSitemap
from landing_pages.sitemaps import PageSitemap

from . import views

sitemaps = {
    'posts': PostSitemap,
    'flatpages': FlatPageSitemap,
    'single_pages': PageSitemap,
}

# https://overiq.com/django-1-10/handling-media-files-in-django/
regular_patterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('p/', include('landing_pages.urls', namespace='pages')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml/', index, {'sitemaps': sitemaps}),
    path('sitemap-<str:section>.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
flatpage_patterns = [
    # https://docs.djangoproject.com/en/3.2/ref/contrib/flatpages/#using-the-urlconf

    path('privacy-policy/', staticviews.flatpage, {'url': '/privacy-policy/'}, name='privacy-policy'),
    path('', staticviews.flatpage, {'url': '/home/'}, name='home'),
    path('home/', views.index, name='index'),
    re_path(r'^(?P<url>.*/)$', staticviews.flatpage),
]

media_root = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_root = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = regular_patterns + media_root + static_root + flatpage_patterns
