from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from events.models import Event

class IndexEventView(ListView):
    model = Event
    template_name = 'CBF/post-home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexEventView, self).get_context_data(**kwargs)
        context['last_element'] = Event.objects.last()
        context['elements'] = Event.objects.all().order_by('date_created')[0:6]
        return context


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['elements'] = Event.objects.all()
        return context
