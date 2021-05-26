from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.IndexView.as_view(template_name='conferences/index.html'),
         name='home'),
    path('conference/<int:pk>/',
         views.ConferenceView.as_view(template_name='conferences/conference.html'),
         name='conference'),
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
    path('submission/<int:conf_pk>/',
         views.SubmissionCreationView.as_view(template_name='submissions/create.html'),
         name='submission_create'),
    path('submission/update/<int:pk>/',
         views.SubmissionUpdateView.as_view(template_name='submissions/update.html'),
         name='submission_update'),
    # path('submission/delete/<int:pk>',
    #      views.SubmissionDeleteView.as_view(),
    #      name='submission_delete'),
    path('submission/delete/<int:pk>', views.delete_submission, name='submission_delete'),
    path('submission/accepted/<int:pk>/', views.accept_submission, name='submission_accepted'),
    path('submission/refused/<int:pk>/', views.refuse_submission, name='submission_refused'),
]

handler404 = 'conferences.views.error_404_handler'
handler500 = 'conferences.views.error_500_handler'
