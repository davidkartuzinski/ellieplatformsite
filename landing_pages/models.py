from django.db import models
from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    result = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='campaign_tags')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=50)
    # slug = models.SlugField()
    description = models.TextField()
    content = HTMLField()
    schema = models.JSONField()
    tags = models.ManyToManyField(Tag, related_name='page_tags')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
