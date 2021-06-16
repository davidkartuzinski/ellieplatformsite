from django.contrib import admin
from .models import Post, Category, Profile


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'published_date', 'status')
    list_filter = ('status', 'created_date', 'published_date', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}  # SEO friendly URLs
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')


admin.site.register(Category)
admin.site.register(Profile)

# https://stackoverflow.com/questions/2466373/create-hyperlink-in-django-template-of-object-that-has-a-space/2468295#2468295
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"post_slug": "title"}
#
#
# admin.site.register(Post, PostAdmin)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
# https://www.codesnail.com/designing-the-blog-data-schema-django-blog-2/
