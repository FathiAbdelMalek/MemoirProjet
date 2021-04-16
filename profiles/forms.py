from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['birth_date', 'sexe',
                  'country', 'work_place', 'degree', 'speciality', 'web_site']
