from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class AboutUsAppHook(CMSApp):
    app_name = 'about_us'
    name = _("Sobre nosotros")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["about_us.urls"]


apphook_pool.register(AboutUsAppHook)
