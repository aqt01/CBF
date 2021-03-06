from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class EventApphook(CMSApp):
    app_name = 'events'
    name = _("Eventos")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["events.urls"]


apphook_pool.register(EventApphook)
