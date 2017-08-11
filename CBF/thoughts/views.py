from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from thoughts.models import Thought
import ipdb


class IndexThoughtView(ListView):
    model = Thought
    template_name = 'CBF/post-home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexThoughtView, self).get_context_data(**kwargs)
        context['last_element'] = Thought.objects.all().last()
        context['elements'] = Thought.objects.all().order_by('date_created')[0:6]
        return context




class ThoughtDetailView(DetailView):
    model = Thought

    def get_context_data(self, **kwargs):
        context = super(ThoughtDetailView, self).get_context_data(**kwargs)
        context['other_elements'] = Thought.objects.all()
        return context
