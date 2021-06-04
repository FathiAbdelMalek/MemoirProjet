from django.contrib import admin

from conferences.admin import site
from . import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'country', 'work_place', 'degree', 'speciality')
    list_filter = ('sex', 'degree', 'speciality', 'country')


site.register(models.Profile, ProfileAdmin)
