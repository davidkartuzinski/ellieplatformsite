from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     post_slug = models.SlugField(max_length=60, unique=True)
#     header_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
