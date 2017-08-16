from django.views.generic import TemplateView

from sermons.models import Sermon
from thoughts.models import Thought
from events.models import Event

from django.contrib.postgres.search import SearchQuery
from django.shortcuts import render

from CBF.utils import elements_text_search


class IndexHomeView(TemplateView):
    template_name = 'CBF/home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexHomeView, self).get_context_data(**kwargs)
        context['last_element'] = Event.objects.last()
        context['events'] = Event.objects.all()[1:3]
        context['sermons'] = Sermon.objects.all()[:3]
        context['thoughts'] = Thought.objects.all()[:3]

        return context


class SearchResult(TemplateView):
    template_name = 'CBF/elements-list.html'

    def post(self, request, **kwargs):
        print(request.POST)
        elements= full_text_search(request.POST['search'])
        return render(request, self.template_name, {'elements': elements})
