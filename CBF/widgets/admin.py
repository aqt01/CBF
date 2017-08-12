from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from .models import Banner, SliderImage, BannerGroup
from .models import Slider, PrincipleGroup, Principle


class BannerInLine(admin.TabularInline):
    model = Banner
    extra = 1


class BannerGroupAdmin(PageExtensionAdmin):
    inlines = [
        BannerInLine,
    ]


class SliderImageInLine(admin.TabularInline):
    model = SliderImage
    extra = 1


class SliderAdmin(PageExtensionAdmin):
    inlines = [
        SliderImageInLine,
    ]


class PrincipleInLine(admin.TabularInline):
    model = Principle
    extra = 1


class PrincipleGroupAdmin(PageExtensionAdmin):
    inlines = [
        PrincipleInLine,
    ]


admin.site.register(BannerGroup, BannerGroupAdmin)
admin.site.register(Banner)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SliderImage)
admin.site.register(PrincipleGroup, PrincipleGroupAdmin)
admin.site.register(Principle)

