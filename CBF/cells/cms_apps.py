from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CellApphook(CMSApp):
    app_name = 'cells'
    name = _("Celulas")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["cells.urls"]


apphook_pool.register(CellApphook)
