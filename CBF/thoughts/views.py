from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from thoughts.models import Thought
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from CBF.utils import elements_related_by_tags


class IndexThoughtViewMixin(object):

    def get_context_data(self, **kwargs):
        context = super(IndexThoughtViewMixin, self).get_context_data(**kwargs)
        sermons = Thought.objects.all()
        context['element_name'] = sermons[0]._meta.verbose_name_plural
        context['paginator'] = Paginator(sermons, 6)
        page = self.request.GET.get('page')

        if (page is not None):
            self.template_name = 'CBF/elements-list.html'

            try:
                context['elements'] = context['paginator'].page(page)

            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                context['elements'] = context['paginator'].page(1)

            except EmptyPage:
                context['elements'] = context['paginator'].page(context['paginator'].num_pages)

        else:
            context['last_element'] = Thought.objects.first()
            context['elements'] = Thought.objects.all().order_by('date_created')[0:6]

        return context


class IndexThoughtView(IndexThoughtViewMixin, ListView):
    model = Thought
    template_name = 'CBF/post-home.html'
    context_object_name = 'thoughts'
    paginate_by = 6


class ThoughtDetailView(DetailView):
    model = Thought
    template_name = 'CBF/element-detail.html'
    slug_field = 'slug'
    context_object_name = 'element'

    def get_context_data(self, **kwargs):
        context = super(ThoughtDetailView, self).get_context_data(**kwargs)
        # We get the object on this detail view and search for related object by tags
        obj = self.get_object()
        tags = obj.get_tags()
        context['elements'] = elements_related_by_tags(tags, Thought, self.get_object())
        context['element_name'] = self.object._meta.verbose_name_plural
        return context
