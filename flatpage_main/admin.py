from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from .models import *


class NewFlatpageInline(admin.StackedInline):
    model = NewFlatpage
    verbose_name = "Content"



class FlatPageNewAdmin(FlatPageAdmin):
    inlines = [NewFlatpageInline]
    fieldsets = (
        (None, {'fields': ('url', 'title', 'sites')}),
        (('Advanced options'), {
            'fields': ('template_name',),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')
    save_as = True
    save_on_top = True


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)

