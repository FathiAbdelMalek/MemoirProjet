from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',
         views.ProfileView.as_view(template_name='profiles/profile.html'),
         name="profile"),
    path('<int:pk>/update/',
         views.ProfileUpdateView.as_view(template_name='profiles/profile_update.html'),
         name='profile_update'),
]
