from django.urls import path
from . import views


urlpatterns = [
    path('', view, name='admin_login'),
]
