from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from .models import BannerGroup, Slider, PrincipleGroup
from .models import Principle, SliderImage
from cms.utils import get_language_list
from cms.models.pagemodel import Page


@toolbar_pool.register
class BannerGroupToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = BannerGroup

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item in position 0 (at the top of the menu)
                current_page_menu.add_modal_item(_('Banners'), url=url,
                                                 disabled=not self.toolbar.edit_mode, position=0)

@toolbar_pool.register
class PrincipleGroupToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = PrincipleGroup

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        print(self.app_path)
        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if self.app_path == 'about_us':
                # adds a toolbar item in position 0 (at the top of the menu)
                current_page_menu.add_modal_item(_('Principios'), url=url,
                    disabled=not self.toolbar.edit_mode, position=2)

# The the slider attached to the first page created
@toolbar_pool.register
class SliderToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = Slider

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if self.app_path == 'home':
                # adds a toolbar item in position 0 (at the top of the menu)
                current_page_menu.add_modal_item(_('Slider'), url=url,
                                                 disabled=not self.toolbar.edit_mode, position=1)
