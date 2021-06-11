from django.contrib import admin
from .models import Post, Category



# Register your models here.

admin.site.register(Post)
admin.site.register(Category)


# https://stackoverflow.com/questions/2466373/create-hyperlink-in-django-template-of-object-that-has-a-space/2468295#2468295
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"post_slug": "title"}
#
#
# admin.site.register(Post, PostAdmin)





