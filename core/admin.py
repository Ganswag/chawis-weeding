from django.contrib import admin
from .models import SiteData


class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created_at')


class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('site_name', )

admin.site.register(SiteData, SiteDataAdmin)
