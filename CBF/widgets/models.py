from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from CBF.abstract_models import CommonWidgetInfo

from fontawesome.fields import IconField


class Principle(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=150, blank=True)
    content = models.CharField(verbose_name="Contenido", max_length=150, blank=True)
    icon = IconField()

    def __str__(self):
        return self.title


class PrincipleGroup(PageExtension):
    principles = models.ManyToManyField(Principle, blank=True)

    def copy_relations(self, oldinstance, language):
        for principle in oldinstance.principles.all():
            principle.pk = None
            principle.principlesgroupextension = self
            principle.save()


class Banner(PageExtension, CommonWidgetInfo):

    def __str__(self):
        return self.name


class HomeBanner(PageExtension):
    banners = models.ManyToManyField(Banner, blank=True)

    def copy_relations(self, oldinstance, language):
        for banner in oldinstance.banners.all():
            banner.pk = None
            banner.homebannerextension = self
            banner.save()


class SliderImage(CommonWidgetInfo):

    def __str__(self):
        return self.title


class Slider(PageExtension):
    slides = models.ManyToManyField(SliderImage, blank=True)

    def copy_relations(self, oldinstance, language):
        for slider in oldinstance.slides.all():
            slider.pk = None
            slider.sliderextension = self
            slider.save()


extension_pool.register(PrincipleGroup)
extension_pool.register(Banner)
extension_pool.register(HomeBanner)
extension_pool.register(Slider)
