from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.core.mail import send_mail
from .models import Conference, Submission
from .forms import ConferenceCreationForm, ConferenceUpdateForm, SubmissionCreationForm, SubmissionUpdateForm


class IndexView(generic.ListView):
    model = Conference

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demand_list'] = Submission.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class ConferenceCreationView(generic.CreateView):
    model = Conference
    form_class = ConferenceCreationForm

    def form_valid(self, form):
        conference = form.save(commit=False)
        conference.organizer = self.request.user
        conference.save()
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class ConferenceUpdateView(generic.UpdateView):
    model = Conference
    form_class = ConferenceUpdateForm
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.save()
        return redirect('home')


@login_required()
def delete_conference(request, pk):
    Conference.objects.filter(id=pk).delete()
    return redirect('home')


@method_decorator(login_required, name='dispatch')
class ConferenceDeleteView(generic.DeleteView):
    model = Conference
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class DemandCreationView(generic.CreateView):
    model = Submission
    form_class = SubmissionCreationForm
    pk_url_kwarg = 'conf_pk'

    def form_valid(self, form):
        demand = form.save(commit=False)
        demand.user = self.request.user
        demand.conference = Conference.objects.get(id=self.kwargs['conf_pk'])
        demand.save()
        messages.success(self.request, 'You demand to subscribe successfully')
        message = ""
        message += str(demand.user)
        message += " has demand to submit in your conference "
        message += str(demand.conference.title)
        send_mail(
            'a demand for submission',
            message,
            'abdelmalek.fathi.2001@gmail.com',
            [demand.conference.organizer.email]
        )
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class DemandUpdateView(generic.UpdateView):
    model = Submission
    form_class = SubmissionUpdateForm
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.save()
        return redirect('home')


@login_required()
def delete_demand(request, pk):
    Submission.objects.filter(id=pk).delete()
    return redirect('home')


@method_decorator(login_required, name='dispatch')
class DemandDeleteView(generic.DeleteView):
    model = Submission
    success_url = reverse_lazy('home')


@login_required()
def accept_demand(request, pk):
    demand = Submission.objects.get(id=pk)
    demand.status = 1
    demand.save()
    message = ""
    message += str(demand.user)
    message += " has accepted your demand to submit in "
    message += str(demand.conference.title)
    send_mail(
        'a demand for submission',
        message,
        'abdelmalek.fathi.2001@gmail.com',
        [demand.conference.organizer.email]
    )
    messages.success(request, 'The demand has ben accepted successfully')
    return redirect('home')


@login_required()
def refuse_demand(request, pk):
    demand = Submission.objects.get(id=pk)
    demand.status = 2
    demand.save()
    message = ""
    message += str(demand.user)
    message += " has refused your demand to submit in "
    message += str(demand.conference.title)
    send_mail(
        'a demand for submission',
        message,
        'abdelmalek.fathi.2001@gmail.com',
        [demand.conference.organizer.email]
    )
    messages.success(request, 'The demand has ben refused successfully')
    return redirect('home')
