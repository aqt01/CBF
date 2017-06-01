from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Preach

class IndexPreachView(ListView):
    model = Preach
    #template_name = 'preach_list.html'
    paginate_by = 6


class PreachDetailView(DetailView):
    model = Preach
    #template_name = 'preach_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PreachDetailView, self).get_context_data(**kwargs)
        context['other_events'] = Event.objects.exclude(pk=self.get_object().pk)
        return context
