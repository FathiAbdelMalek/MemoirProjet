from django import forms
from .models import Conference, Demand


class ConferenceCreationForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ['title', 'description', 'date', 'last_date_for_submit', 'last_date_for_confirm', 'last_date_for_pay', 'place']


class ConferenceUpdateForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ['title', 'description', 'date', 'last_date_for_submit', 'last_date_for_confirm', 'last_date_for_pay', 'place']


class DemandCreationForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['first_name', 'last_name', 'email', 'abstract', 'article', 'authors']


class DemandUpdateForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['first_name', 'last_name', 'email', 'abstract', 'article', 'authors']
