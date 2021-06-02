from django.urls import path
from . import views

urlpatterns = [
    path('<slug:username>/',
         views.ProfileView.as_view(template_name='profiles/profile.html'),
         name="profile"),
    path('public/<slug:username>/',
         views.PublicProfileView.as_view(template_name='profiles/public_profile.html'),
         name='public_profile'),
    path('<int:pk>/update/',
         views.ProfileUpdateView.as_view(template_name='profiles/profile_update.html'),
         name='profile_update'),
]
