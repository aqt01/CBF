from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SermonApphook(CMSApp):
    app_name = 'sermons'
    name = _("Sermones")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["sermons.urls"]


apphook_pool.register(SermonApphook)
