from django.contrib import admin

from conferences.admin import site
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin', 'is_superuser')


site.register(models.User, UserAdmin)
