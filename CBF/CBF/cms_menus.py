from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu


class MainMenu(CMSAttachMenu):
    """This modifier extends the resources page to include the resources subpages."""
    name = _("Menu principal")

    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_("Eventos"), "/eventos/", 1)
        n2 = NavigationNode(_("Sermones"), "/sermones/", 2)
        n3 = NavigationNode(_("Celulas"), "/celulas/", 3)
        n4 = NavigationNode(_("Reflexiones"), "/reflexiones/", 4)
        n5 = NavigationNode(_("Libros"), "/libros/", 5)
        n6 = NavigationNode(_("Conocenos"), "/conocenos/", 6)

        nodes.append(n1)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        nodes.append(n5)
        nodes.append(n6)

        return nodes


menu_pool.register_menu(MainMenu)
