from django.views.generic import TemplateView

from membership.models import Member
from widgets.models import PrincipleGroup, BannerGroup


class IndexAboutUsMixinView(object):

    def get_context_data(self, **kwargs):
        context = super(IndexAboutUsMixinView, self).get_context_data(**kwargs)
        context['main_leaders'] = Member.objects.filter(role__lte=2)
        context['leaders'] = Member.objects.filter(role__gt=2, role__lte=4)
        try:
            context['principle_group'] = PrincipleGroup.objects.filter(extended_object__application_namespace='about_us').first()
            banner_group = BannerGroup.objects.filter(extended_object__application_namespace='about_us').first()
            context['banner'] = banner_group.banner_set.first()
        except Exception:
            context['principle_group'] = None
            context['banner'] = None
        return context


class IndexAboutUsView(IndexAboutUsMixinView, TemplateView):
    template_name = 'CBF/about-us.html'
