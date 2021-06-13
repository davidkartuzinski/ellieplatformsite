from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Profile Model
# https://learnitfree.org/django-custom-user-model/

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField(null=True, max_length=300)
    profile_pic = models.ImageField(default='default-profile-pic.jpeg', upload_to='profiles-pics')

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['user']

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


# Post Model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    header_image = models.ImageField(upload_to='blog/%Y/%m/%d', height_field=None, width_field=None, max_length=100)
    post_content = RichTextUploadingField()
    intro = RichTextField(max_length=160)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    meta_description = models.TextField(max_length=160, default='meta description')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
