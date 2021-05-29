from django import forms
from .models import Conference, Submission


class ConferenceCreationForm(forms.ModelForm):

    date = forms.DateField(label='Conference Date', widget=forms.SelectDateWidget)
    submission_deadline = forms.DateField(label='Submission Deadline', widget=forms.SelectDateWidget)
    confirmation_deadline = forms.DateField(label='Confirmation Deadline', widget=forms.SelectDateWidget)
    payment_deadline = forms.DateField(label='Payment Deadline', widget=forms.SelectDateWidget)

    class Meta:
        model = Conference
        fields = ['title', 'description', 'date', 'submission_deadline', 'confirmation_deadline', 'payment_deadline',
                  'pre_price', 'place']


class ConferenceUpdateForm(forms.ModelForm):

    date = forms.DateField(label='Conference Date', widget=forms.SelectDateWidget)
    submission_deadline = forms.DateField(label='Submission Deadline', widget=forms.SelectDateWidget)
    confirmation_deadline = forms.DateField(label='Confirmation Deadline', widget=forms.SelectDateWidget)
    payment_deadline = forms.DateField(label='Payment Deadline', widget=forms.SelectDateWidget)

    class Meta:
        model = Conference
        fields = ['title', 'description', 'date', 'submission_deadline', 'confirmation_deadline', 'payment_deadline',
                  'pre_price', 'place']


class SubmissionCreationForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['first_name', 'last_name', 'email', 'article_name', 'abstract', 'article', 'authors']


class SubmissionUpdateForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['first_name', 'last_name', 'email', 'article_name', 'abstract', 'article', 'authors']
