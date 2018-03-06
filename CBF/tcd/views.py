from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from .models import TCDSubscription
from .forms import TCDSubscriptionForm
from django.views.generic import TemplateView


class TCDSubscriptionView(TemplateView):
    template_name = 'TCD/index.html'


class TCDRegisterView(CreateView):
    form_class = TCDSubscriptionForm
    model = TCDSubscription
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    template_name = 'TCD/form.html'
    success_url = reverse_lazy('tcd:thanks')


class TCDSubscriptionViewThanks(TemplateView):
    template_name = 'TCD/form.html'
