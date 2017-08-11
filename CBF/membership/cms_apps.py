from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class MembershipApphook(CMSApp):
    app_name = 'membership'
    name = _("Miembros")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["membership.urls"]


apphook_pool.register(MembershipApphook)
