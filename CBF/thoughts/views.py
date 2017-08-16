from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from thoughts.models import Thought
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexThoughtView(ListView):
    model = Thought
    template_name = 'CBF/post-home.html'
    context_object_name = 'thoughts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(IndexThoughtView, self).get_context_data(**kwargs)
        thoughts = Thought.objects.all()
        context['paginator'] = Paginator(thoughts, 6)
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
            context['last_element'] = Thought.objects.first()
            context['elements'] = Thought.objects.all().order_by('date_created')[0:6]

        return context



class ThoughtDetailView(DetailView):
    model = Thought

    def get_context_data(self, **kwargs):
        context = super(ThoughtDetailView, self).get_context_data(**kwargs)
        context['other_elements'] = Thought.objects.all()
        return context
