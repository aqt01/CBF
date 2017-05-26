from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Preach

class IndexPreachView(ListView):
    model = Preach
    #template_name = 'events_list.html'
    paginate_by = 6


class EventDetailView(DetailView):
    #template_name = 'events_detail.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['other_events'] = Event.objects.exclude(pk=self.get_object().pk)
        return context




# Create your views here.
