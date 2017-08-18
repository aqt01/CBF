from django.views.generic import TemplateView

from membership.models import Member


class IndexAboutUsView(TemplateView):
    template_name = 'CBF/about-us.html'

    def get_context_data(self, **kwargs):
        context = super(IndexAboutUsView, self).get_context_data(**kwargs)
        context['main_leaders'] = Member.objects.filter(role__lte=2)
        context['leaders'] = Member.objects.filter(role__gt=2, role__lte=4)
        print(context['leaders'])
        return context
