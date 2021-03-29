from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreationForm
from profiles.models import Profile


class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(
            user=user,
        )
        login(self.request, user)
        return redirect('profile', user.pk)
