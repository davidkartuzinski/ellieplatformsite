from django.contrib import admin

from landing_pages.models import (Page)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True

