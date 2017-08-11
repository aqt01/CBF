from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from .models import BannerExtension, SliderExtension, PrincipleGroupExtension
from cms.utils import get_language_list
from cms.models.pagemodel import Page


@toolbar_pool.register
class BannerExtensionToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = BannerExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu and self.toolbar.edit_mode:
            # create a sub menu labelled "Ratings" at position 1 in the menu
            sub_menu = self._get_sub_menu(
                current_page_menu, 'submenu_label', 'Editar elementos', position=1
                )

            # retrieves the instances of the current title extension (if any)
            # and the toolbar item URL
            urls = self.get_title_extension_admin()

            # we now also need to get the titleset (i.e. different language titles)
            # for this page
            page = self._get_page()
            titleset = page.title_set.filter(language__in=get_language_list(page.site_id))

            # create a 3-tuple of (title_extension, url, title)
            nodes = [(title_extension, url, title.title) for (
                (title_extension, url), title) in zip(urls, titleset)
                ]

            # cycle through the list of nodes
            for title_extension, url, title in nodes:

                # adds toolbar items
                sub_menu.add_modal_item(
                    'Editar banners en %s' % title, url=url, disabled=not self.toolbar.edit_mode
                    )

# The the slider attached to the first page created
@toolbar_pool.register
class SliderExtensionToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = SliderExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu and self.toolbar.edit_mode:
            # create a sub menu labelled "Ratings" at position 1 in the menu
            sub_menu = self._get_sub_menu(
                current_page_menu, 'submenu_label', 'Editar elementos', position=2
                )

            # retrieves the instances of the current title extension (if any)
            # and the toolbar item URL
            urls = self.get_title_extension_admin()

            # we now also need to get the titleset (i.e. different language titles)
            # for this page
            page = self._get_page()
            titleset = page.title_set.filter(language__in=get_language_list(page.site_id))

            # create a 3-tuple of (title_extension, url, title)
            nodes = [(title_extension, url, title.title) for (
                (title_extension, url), title) in zip(urls, titleset)
                ]

            # cycle through the list of nodes
            for title_extension, url, title in nodes:
                if Page.objects.first().get_title() == title:
                    # adds toolbar items
                    sub_menu.add_modal_item(
                        'Editar slider en %s' % title, url=url, disabled=not self.toolbar.edit_mode
                    )




@toolbar_pool.register
class SliderExtension(ExtensionToolbar):
    # defines the model for the current toolbar
    model = SliderExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item in position 0 (at the top of the menu)
                current_page_menu.add_modal_item(_('Slider'), url=url,
                    disabled=not self.toolbar.edit_mode, position=0)


@toolbar_pool.register
class PrincipleExtensionToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = PrincipleGroupExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu and self.toolbar.edit_mode:
            # create a sub menu labelled "Ratings" at position 1 in the menu
            sub_menu = self._get_sub_menu(
                current_page_menu, 'submenu_label', 'Editar elementos', position=2
                )

            # retrieves the instances of the current title extension (if any)
            # and the toolbar item URL
            urls = self.get_title_extension_admin()

            # we now also need to get the titleset (i.e. different language titles)
            # for this page
            page = self._get_page()
            titleset = page.title_set.filter(language__in=get_language_list(page.site_id))

            # create a 3-tuple of (title_extension, url, title)
            nodes = [(title_extension, url, title.title) for (
                (title_extension, url), title) in zip(urls, titleset)
                ]

            # cycle through the list of nodes
            for title_extension, url, title in nodes:
                print (title)
                if title == 'Conócenos':
                    # adds toolbar items
                    sub_menu.add_modal_item(
                        'Editar principios en %s' % title, url=url, disabled=not self.toolbar.edit_mode
                    )
