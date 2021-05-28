from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Profile
from .forms import ProfileUpdateForm
from conferences.models import Conference, Submission


User = get_user_model()


class ProfileView(generic.DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['conferences'] = Conference.objects.filter(organizer=self.request.user)
        context['submissions'] = Submission.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(generic.UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    pk_url_kwarg = 'pk'
    context_object_name = 'profile'

    def form_valid(self, form):
        form.save()
        return redirect('profile', form.user.pk)
