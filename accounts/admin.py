from atexit import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'date_joined', 'last_login', 'user_group', 'sub_group', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin,)
admin.site.register(Group)
admin.site.register(SubGroup)
