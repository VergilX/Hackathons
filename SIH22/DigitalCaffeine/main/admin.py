from django.contrib import admin

from .models import *
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ("code", "status", "user")
    search_fields = ("code", "user")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Device, DeviceAdmin)