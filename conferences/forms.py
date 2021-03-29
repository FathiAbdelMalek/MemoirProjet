from django import forms
from .models import Conference, Demand


class ConferenceCreationForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ['title', 'description', 'last_date', 'place']


class ConferenceUpdateForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ['title', 'description', 'last_date', 'place', 'enabled']


class DemandCreationForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['note']


class DemandUpdateForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['note']
