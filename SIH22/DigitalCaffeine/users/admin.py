from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import *

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_teacher')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    # filters are default, so setting them as nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# registering to admin
admin.site.register(User, UserAdmin)