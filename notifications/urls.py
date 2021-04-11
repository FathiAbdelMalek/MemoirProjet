from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_notifications, name='notifications'),
    path('<int:pk>/', views.delete_notifications, name='notification_delete')
]
