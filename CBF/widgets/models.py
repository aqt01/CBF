from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from cms.models.fields import PageField

from CBF.abstract_models import CommonWidgetInfo

from fontawesome.fields import IconField


class PrincipleGroup(PageExtension):
    pass

class Principle(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=150, blank=True)
    content = models.CharField(verbose_name="Contenido", max_length=800, blank=True)
    icon = IconField()
    principles = models.ForeignKey(PrincipleGroup, blank=True)

    def __str__(self):
        return self.title


class BannerGroup(PageExtension):
    pass


class Banner(CommonWidgetInfo):
    banners = models.ForeignKey(BannerGroup, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title



class Slider(PageExtension):
    pass


class SliderImage(CommonWidgetInfo):
    slider = models.ForeignKey(Slider, blank=True)

    def __str__(self):
        return self.title


extension_pool.register(PrincipleGroup)
extension_pool.register(BannerGroup)
extension_pool.register(Slider)
