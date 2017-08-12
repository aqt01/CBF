from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class HomeApphook(CMSApp):
    app_name = 'home'
    name = _("Pagina de inicio")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["home.urls"]


apphook_pool.register(HomeApphook)
