from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Profile
from .forms import ProfileUpdateForm
from conferences.models import Conference, Submission


User = get_user_model()


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.DetailView):
    model = Profile

    def get_object(self, queryset=None):
        obj = {
            'user': self.request.user,
            'profile': Profile.objects.get(user=self.request.user),
            'conferences': Conference.objects.filter(organizer=self.request.user),
            'submissions': Submission.objects.filter(user=self.request.user)
        }
        self.request.session['page'] = self.request.path
        return obj


class PublicProfileView(generic.DetailView):
    model = Profile

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.kwargs['username'])
        obj = {
            'user': user,
            'profile': Profile.objects.get(user=user),
            'conferences': Conference.objects.filter(organizer=user),
            'submissions': Submission.objects.filter(user=user)
        }
        self.request.session['page'] = self.request.path
        return obj


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(generic.UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    pk_url_kwarg = 'pk'
    context_object_name = 'profile'

    def form_valid(self, form):
        form.save()
        return redirect(self.request.session['page'])
