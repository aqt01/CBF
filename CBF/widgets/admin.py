from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from .models import BannerExtension, SliderImageExtension, HomeBannerExtension
from .models import SliderExtension, PrincipleGroupExtension, PrincipleExtension



class HomeBannerExtensionAdmin(PageExtensionAdmin):
    pass


class BannerExtensionAdmin(PageExtensionAdmin):
    pass


class SliderExtensionAdmin(PageExtensionAdmin):
    pass


class SliderImageExtensionAdmin(PageExtensionAdmin):
    pass


class PrincipleExtensionAdmin(PageExtensionAdmin):
    pass


admin.site.register(HomeBannerExtension, HomeBannerExtensionAdmin)
admin.site.register(BannerExtension, BannerExtensionAdmin)
admin.site.register(SliderExtension, SliderExtensionAdmin)
admin.site.register(SliderImageExtension, SliderImageExtensionAdmin)
admin.site.register(PrincipleGroupExtension, PrincipleExtensionAdmin)
admin.site.register(PrincipleExtension, PrincipleExtensionAdmin)
