from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField
from CBF.abstract_models import CommonWidgetInfo
# Create your models here.


class PrincipleExtension(PageExtension):
    title = models.CharField(verbose_name="Titulo en banner de reflexiones", max_length=150, blank=True)
    content = models.CharField(verbose_name="Contenido en banner de reflexiones", max_length=150, blank=True)
    icon = FilerImageField(blank=True, null=True,
                           verbose_name="Imagen del banner",
                           help_text="Tamaño sugerido: 1024x764")

    def __str__(self):
        return self.name


class PrincipleGroupExtension(PageExtension):
    principles = models.ManyToManyField(PrincipleExtension, blank=True)


class BannerExtension(PageExtension, CommonWidgetInfo):

    def __str__(self):
        return self.name


class HomeBannerExtension(PageExtension):
    thought_banner_title = models.CharField(verbose_name="Titulo en banner de reflexiones", max_length=150, blank=True)
    thought_banner_content = models.CharField(verbose_name="Contenido en banner de reflexiones", max_length=150, blank=True)
    thought_banner = models.ImageField(upload_to='banners', blank=True)
    sermon_banner_title = models.CharField(verbose_name="Titulo en banner de sermones", max_length=150, blank=True)
    sermon_banner_content = models.CharField(verbose_name="Contenido en banner de sermones", max_length=150, blank=True)
    sermon_banner = models.ImageField(upload_to='banners', blank=True)
    followus_banner_title = models.CharField(verbose_name="Titulo en banner de siguenos", max_length=150, blank=True)
    followus_banner_content = models.CharField(verbose_name="Contenido en banner de siguenos", max_length=150, blank=True)
    followus_banner = models.ImageField(upload_to='banners', blank=True)


class SliderImageExtension(PageExtension, CommonWidgetInfo):

    def __str__(self):
        return self.name


class SliderExtension(PageExtension):
    slider = models.ManyToManyField(SliderImageExtension, blank=True)

    def copy_relations(self, oldinstance, language):
        for slider in oldinstance.slider.all():
            slider.pk = None
            slider.sliderextension = self
            slider.save()


extension_pool.register(PrincipleGroupExtension)
extension_pool.register(BannerExtension)
extension_pool.register(SliderExtension)
