from django.contrib import admin

from landing_pages.models import (
    Tag, Campaign, Page)


admin.site.register(Tag)
admin.site.register(Campaign)
admin.site.register(Page)
