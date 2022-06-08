from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import *

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    # filters are default, so setting them as nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class RefereeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'job', 'phone')
    search_fields = ('name', 'phone')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'qualification')
    search_fields = ('user', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'job')
    search_fields = ('user', )

    filter_horizontal = ()
    list_filter = ()


admin.site.register(Language)
admin.site.register(Certificate)
admin.site.register(Skill)
admin.site.register(Club)
admin.site.register(Referee)
admin.site.register(Education, EducationAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(User, UserAdmin)