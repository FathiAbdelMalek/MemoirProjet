from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, label='First name', widget=forms.TextInput)
    last_name = forms.CharField(max_length=20, label='Last name', widget=forms.TextInput)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'sexe', 'country', 'work_place', 'degree', 'speciality', 'web_site']
