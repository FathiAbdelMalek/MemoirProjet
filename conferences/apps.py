from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ElconferenceAdminConfig(AdminConfig):
    default_site = 'conferences.admin.ElconferencesAdmin'


class ConferencesConfig(AppConfig):
    name = 'conferences'
