from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from .models import Banner, SliderImage, HomeBanner
from .models import Slider, PrincipleGroup, Principle


class HomeBannerAdmin(PageExtensionAdmin):
    pass


class SliderImageInLine(admin.TabularInline):
    model = SliderImage
    extra = 1


class SliderAdmin(PageExtensionAdmin):
    pass


class PrincipleGroupAdmin(PageExtensionAdmin):
    pass


admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(Banner)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SliderImage)
admin.site.register(Principle)
admin.site.register(PrincipleGroup, PrincipleGroupAdmin)
