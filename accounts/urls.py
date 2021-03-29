from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',
         views.RegisterView.as_view(template_name='accounts/register.html'),
         name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password/change/1.html'),
         name='password_change'),
    path('password_change/done',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password/change/2.html'),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password/reset/1.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password/reset/2.html'),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password/reset/3.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password/reset/4.html'),
         name='password_reset_complete'),
]
