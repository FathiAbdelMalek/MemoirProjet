from django.shortcuts import redirect
from django.contrib.auth import login
from django.views import generic

from conferences.models import Author
from .models import User
from .forms import UserCreationForm
from profiles.models import Profile


class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        profile = Profile(
            user=user
        )
        profile.save()
        author = Author(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            email=form.cleaned_data.get('email'),
        )
        author.save()
        login(self.request, user)
        return redirect('profile', user.pk)
