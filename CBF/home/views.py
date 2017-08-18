from django.views.generic import TemplateView
from django.shortcuts import render
from CBF.utils import elements_text_search
from django.views.generic.edit import FormView


from sermons.models import Sermon
from thoughts.models import Thought
from events.models import Event
from subscribers.models import Subscriber
from subscribers.forms import SubscriberForm


class ThanksView(TemplateView):
    template_name = 'CBF/thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        return context


class IndexHomeView(FormView):
    form_class = SubscriberForm
    template_name = 'CBF/home.html'
    success_url = '/gracias'

    def get_context_data(self, **kwargs):
        context = super(IndexHomeView, self).get_context_data(**kwargs)
        context['last_element'] = Event.objects.last()
        context['events'] = Event.objects.all()[1:3]
        context['sermons'] = Sermon.objects.all()[:3]
        context['thoughts'] = Thought.objects.all()[:3]
        return context

    def form_valid(self, form):
        subscriber = Subscriber.objects.create(email=form.cleaned_data['email'])
        return super(IndexHomeView, self).form_valid(form)



class SearchResult(TemplateView):
    template_name = 'CBF/elements-list.html'

    def post(self, request, **kwargs):
        print(request.POST)
        elements = elements_text_search(request.POST['search'])
        return render(request, self.template_name, {'elements': elements})
