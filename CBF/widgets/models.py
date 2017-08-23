from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from cms.models.fields import PageField

from CBF.abstract_models import CommonWidgetInfo

from fontawesome.fields import IconField


class PrincipleGroup(PageExtension):

    def copy_relations(self, oldinstance, language):
        for principle in oldinstance.principles_set.all():
            principle.pk = None
            principle.principlegroup = self
            principle.save()


class Principle(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=150, blank=True)
    content = models.CharField(verbose_name="Contenido", max_length=150, blank=True)
    icon = IconField()
    principles = models.ForeignKey(PrincipleGroup, blank=True)

    def __str__(self):
        return self.title

    def copy_relations(self, oldinstance, language):
        for principle in oldinstance.principlegroup.all():
            principle.pk = None
            principle.principle = self
            principle.save()


class BannerGroup(PageExtension):

    def copy_relations(self, oldinstance, language):
        for banner in oldinstance.banner_set.all():
            banner.pk = None
            banner.bannergroup = self
            banner.save()


class Banner(CommonWidgetInfo):
    banners = models.ForeignKey(BannerGroup, blank=True)

    class Meta:
        ordering = ['-created']


class Slider(PageExtension):

    def copy_relations(self, oldinstance, language):
        for banner in oldinstance.sliderimage_set.all():
            banner.pk = None
            banner.banner = self
            banner.save()


class SliderImage(CommonWidgetInfo):
    slider = models.ForeignKey(Slider, blank=True)

    def __str__(self):
        return self.title


extension_pool.register(PrincipleGroup)
extension_pool.register(BannerGroup)
extension_pool.register(Slider)
