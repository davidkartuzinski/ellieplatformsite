from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce import models as tinymce_models
from tinymce.models import HTMLField


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post_slug = models.SlugField(max_length=60, unique=True)
    header_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    post_content = tinymce_models.HTMLField()
    intro = HTMLField(default=True, max_length=160)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    meta_description = models.TextField(max_length=160, default='meta description')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
