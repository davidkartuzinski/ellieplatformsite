from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'daily'  # 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
    priority = 0.9

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated


class FlatPageSitemap(Sitemap):
    changefreq = 'daily'  # 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
    priority = 0.9

    class Meta:
        app_label = 'flatpages'

    def items(self):
        return FlatPage.objects.all()

