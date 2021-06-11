from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post_slug = models.SlugField(max_length=60, unique=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    header_image = models.ImageField(upload_to='blog/%Y/%m/%d', height_field=None, width_field=None, max_length=100)
    post_content = RichTextField()
    intro = RichTextField(max_length=160)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    meta_description = models.TextField(max_length=160, default='meta description')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
