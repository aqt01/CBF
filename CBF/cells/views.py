from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from events.models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexCellMixin(object):

    def get_context_data(self, **kwargs):
        context = super(IndexCellMixin, self).get_context_data(**kwargs)
        events = Cell.objects.all()
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
            context['last_element'] = Cell.objects.first()
            context['elements'] = Cell.objects.all().order_by('date_created')[0:6]

        return context


class IndexCellView(IndexCellMixin, ListView):
    model = Cell
    template_name = 'CBF/post-home.html'
    context_object_name = 'cells'
    paginate_by = 6


class CellDetailView(DetailView):
    model = Cell

    def get_context_data(self, **kwargs):
        context = super(CellDetailView, self).get_context_data(**kwargs)
        context['elements'] = Cell.objects.all()
        return context
