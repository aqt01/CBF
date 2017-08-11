from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BookApphook(CMSApp):
    app_name = 'books'
    name = _("Libros")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["books.urls"]


apphook_pool.register(BookApphook)
