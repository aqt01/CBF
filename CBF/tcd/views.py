from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from .models import TCDSubscription
from .forms import TCDSubscriptionForm
from django.views.generic import TemplateView


class TCDSubscriptionView(TemplateView):
    template_name = 'TCD/index.html'


class TCDRegisterView(FormView):
    form_class = TCDSubscriptionForm
    model = TCDSubscription
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    template_name = 'TCD/form.html'
    success_url = reverse_lazy('tcd:thanks')

    def get_context_data(self, **kwargs):
        context = super(TCDRegisterView, self).get_context_data(**kwargs)
        return render(self.request,self.template_name,context)


class TCDSubscriptionViewThanks(TemplateView):
    template_name = 'TCD/form.html'
