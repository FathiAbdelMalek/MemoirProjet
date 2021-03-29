from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from notifications.models import Notification
from .models import Conference, Demand
from .forms import ConferenceCreationForm, ConferenceUpdateForm, DemandCreationForm, DemandUpdateForm


class IndexView(generic.ListView):
    model = Conference

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demands'] = Demand.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class ConferenceCreationView(generic.CreateView):
    model = Conference
    form_class = ConferenceCreationForm

    def form_valid(self, form):
        conference = form.save(commit=False)
        conference.creator = self.request.user
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


@method_decorator(login_required, name='dispatch')
class ConferenceDeleteView(generic.DeleteView):
    model = Conference
    success_url = reverse_lazy('home')


@login_required()
def demand_create(request, conf_pk):
    form = DemandCreationForm()
    if request.method == 'POST':
        form = DemandCreationForm(request.POST)
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = request.user
            demand.conference = Conference.objects.get(id=conf_pk)
            demand.save()
            messages.success(request, 'You demand to subscribe successfully')
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'demands/create.html', context)


@method_decorator(login_required, name='dispatch')
class DemandCreationView(generic.CreateView):
    model = Demand
    form_class = DemandCreationForm
    pk_url_kwarg = 'conf_pk'

    def form_valid(self, form):
        demand = form.save(commit=False)
        demand.user = self.request.user
        demand.conference = Conference.objects.get(id=self.pk_url_kwarg)
        demand.save()
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class DemandUpdateView(generic.UpdateView):
    model = Demand
    form_class = DemandUpdateForm
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.save()
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class DemandDeleteView(generic.DeleteView):
    model = Demand
    success_url = reverse_lazy()


@login_required()
def accept_demand(request, pk):
    # demand = Demand.objects.filter(id=pk)
    # demand.delete()
    messages.success(request, 'The demand has ben accepted successfully')
    return redirect('home')


@login_required()
def refuse_demand(request, pk):
    return redirect('home')
