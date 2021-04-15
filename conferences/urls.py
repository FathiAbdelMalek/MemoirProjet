from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.IndexView.as_view(template_name='conferences/index.html'),
         name='home'),
    path('conferences/new/',
         views.ConferenceCreationView.as_view(template_name='conferences/create.html'),
         name='conference_create'),
    path('conferences/update/<int:pk>/',
         views.ConferenceUpdateView.as_view(template_name='conferences/update.html'),
         name='conference_update'),
    # path('conferences/delete/<int:pk>/',
    #      views.ConferenceDeleteView.as_view(),
    #      name='conference_delete'),
    path('conferences/delete/<int:pk>/', views.delete_conference, name='conference_delete'),
    # path('demand/<int:conf_pk>/',
    #      views.DemandCreationView.as_view(template_name='demands/create.html'),
    #      name='demand_create'),
    path('demand/<int:conf_pk>/', views.demand_create, name='demand_create'),
    path('demand/update/<int:pk>/',
         views.DemandUpdateView.as_view(template_name='demands/update.html'),
         name='demand_update'),
    # path('demand/delete/<int:pk>',
    #      views.DemandDeleteView.as_view(),
    #      name='demand_delete'),
    path('demand/delete/<int:pk>', views.delete_demand, name='demand_delete'),
    path('demand/accepted/<int:pk>/', views.accept_demand, name='demand_accepted'),
    path('demand/refused/<int:pk>/', views.refuse_demand, name='demand_refused'),
]
