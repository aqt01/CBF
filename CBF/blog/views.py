from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Message


class IndexMessageView(ListView):
    model = Message
    #template_name = 'events_list.html'
    paginate_by = 6


class MessageDetailView(DetailView):
    #template_name = 'events_detail.html'
    model = Message

    def get_context_data(self, **kwargs):
        context = super(MessageDetailView, self).get_context_data(**kwargs)
        context['other_events'] = Event.objects.exclude(pk=self.get_object().pk)
        return context

