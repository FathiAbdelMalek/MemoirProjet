from django import forms
from .models import Conference, Submission


class ConferenceCreationForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ['title', 'description', 'date', 'submission_deadline', 'confirmation_deadline', 'payment_deadline', 'price', 'place']


class ConferenceUpdateForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ['title', 'description', 'date', 'submission_deadline', 'confirmation_deadline', 'payment_deadline', 'price', 'place']


class SubmissionCreationForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['first_name', 'last_name', 'email', 'article_name', 'abstract', 'article', 'authors']


class SubmissionUpdateForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['first_name', 'last_name', 'email', 'article_name', 'abstract', 'article', 'authors']
