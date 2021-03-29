from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Profile
from .forms import ProfileUpdateForm
from conferences.models import Conference, Demand


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['conferences'] = Conference.objects.filter(creator=self.request.user)
        context['demands'] = Demand.objects.all()
        context['self_demands'] = Demand.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(generic.UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    pk_url_kwarg = 'pk'
    context_object_name = 'profile'

    def form_valid(self, form):
        profile = form.save()
        return redirect('profile', profile.user.pk)
