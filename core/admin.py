from django.contrib import admin
from .models import SiteData, Guest


class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created_at')


class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('site_name', )

class GuestDataAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'companion_name')


admin.site.register(SiteData, SiteDataAdmin)
admin.site.register(Guest, GuestDataAdmin)