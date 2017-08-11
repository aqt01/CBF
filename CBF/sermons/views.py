from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from sermons.models import Sermon
from django.template import RequestContext
from django.shortcuts import render_to_response

class IndexSermonView(ListView):
    model = Sermon
    template_name = 'CBF/post-home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexSermonView, self).get_context_data(**kwargs)
        context['last_element'] = Sermon.objects.last()
        context['elements'] = Sermon.objects.all().order_by('date_created')[0:6]

        return context


class SermonDetailView(DetailView):
    model = Sermon

    def get_context_data(self, **kwargs):
        context = super(SermonDetailView, self).get_context_data(**kwargs)
        context['elements'] = Sermon.objects.all()
        return context
