from django.views.generic import TemplateView
from django.shortcuts import render
from CBF.utils import elements_text_search, search_elements_related_by_tags
from django.views.generic.edit import FormView

from sermons.models import Sermon
from thoughts.models import Thought
from events.models import Event
from subscribers.models import Subscriber
from subscribers.forms import SubscriberForm
from widgets.models import Slider, BannerGroup


class IndexHomeViewMixin(object):

    def get_context_data(self, **kwargs):
        context = super(IndexHomeViewMixin, self).get_context_data(**kwargs)
        context['last_element'] = Event.objects.last()
        context['last_element_name'] = context['last_element']._meta.verbose_name_plural
        context['events'] = Event.objects.all()[1:3]
        context['event_element_name'] = context['events'][0]._meta.verbose_name_plural

        context['sermons'] = Sermon.objects.all()[:3]
        context['sermon_element_name'] = context['sermons'][0]._meta.verbose_name_plural

        context['thoughts'] = Thought.objects.all()[:3]
        context['thought_element_name'] = context['thoughts'][0]._meta.verbose_name_plural
        slider_group = Slider.objects.filter(extended_object__application_namespace='home').first()
        context['slider_group'] = slider_group.sliderimage_set.all()
        context['banner_group'] = BannerGroup.objects.filter(extended_object__application_namespace='home').first()

        return context

    def form_valid(self, form):
        subscriber = Subscriber.objects.create(email=form.cleaned_data['email'])
        return super(IndexHomeViewMixin, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'CBF/thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        return context


class IndexHomeView(IndexHomeViewMixin, FormView):
    form_class = SubscriberForm
    template_name = 'CBF/home.html'
    success_url = '/gracias'


class SearchResult(TemplateView):
    template_name = 'CBF/elements-list.html'

    def get(self,  request, **kwargs):
        if (request.GET.get('search')):
            elements = elements_text_search(request.GET.get('search'))
        elif (request.GET.get('tag')):
            elements = search_elements_related_by_tags(request.GET.get('tag'),10)
        return render(request, self.template_name, {'elements': elements})
