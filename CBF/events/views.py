from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from events.models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from CBF.utils import elements_related_by_tags


class IndexEventMixin(object):

    def get_context_data(self, **kwargs):
        context = super(IndexEventMixin, self).get_context_data(**kwargs)
        events = Event.objects.all()
        context['element_name'] = events[0]._meta.verbose_name_plural
        context['paginator'] = Paginator(events, 6)
        page = self.request.GET.get('page')

        if (page is not None):
            self.template_name = 'CBF/elements-list.html'

            try:
                context['elements'] = context['paginator'].page(page)

            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                context['elements'] = context['paginator'].page(1)

            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                context['elements'] = context['paginator'].page(context['paginator'].num_pages)

        else:
            context['last_element'] = Event.objects.first()
            context['elements'] = Event.objects.all().order_by('date_created')[0:6]

        return context


class IndexEventView(IndexEventMixin, ListView):
    model = Event
    template_name = 'CBF/post-home.html'
    context_object_name = 'events'
    paginate_by = 6


class EventDetailView(DetailView):
    model = Event
    template_name = 'CBF/element-detail.html'
    slug_field = 'slug'
    context_object_name = 'element'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        # We get the object on this detail view and search for related object by tags
        obj = self.get_object()
        tags = obj.get_tags()
        context['elements'] = elements_related_by_tags(tags, Event)
        context['element_name'] = self.object._meta.verbose_name_plural
        return context
