from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ThoughtApphook(CMSApp):
    app_name = 'thoughts'
    name = _("Reflexiones")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["thoughts.urls"]


apphook_pool.register(ThoughtApphook)
