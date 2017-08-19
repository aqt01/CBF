from django.db import models

from model_utils.models import TimeStampedModel
from filer.fields.image import FilerImageField
from autoslug import AutoSlugField


class CommonElementInfo(TimeStampedModel):
    name = models.CharField(verbose_name="Nombre", max_length=150, unique=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    summary = models.CharField(verbose_name="Resumen", max_length=200, blank=True)
    date_published = models.DateTimeField(verbose_name="Fecha de publicacion", auto_now_add=True)
    is_published = models.BooleanField(verbose_name="Publicado?", default=True)
    img = FilerImageField(blank=True, null=True,
                          verbose_name="Imagen del post",
                          help_text="Tamaño sugerido: 1024x765")
    date_created = models.DateTimeField(verbose_name="Fecha de creacion")


    class Meta:
        abstract = True


class CommonWidgetInfo(TimeStampedModel):
    title = models.CharField(verbose_name="Titulo", max_length=150, blank=True)
    content = models.CharField(verbose_name="Contenido", max_length=150, blank=True)
    img = FilerImageField(blank=True, null=True,
                          verbose_name="Imagen",
                          help_text="Tamaño sugerido: 1024x764")


    class Meta:
        abstract = True


class CommonPostInfo(CommonElementInfo):
    content = models.TextField(verbose_name="Contenido", max_length=1200, blank=True)

    class Meta:
        abstract = True


class CommonLocationInfo(CommonElementInfo):
    name = models.CharField(verbose_name="Nombre", max_length=150)
    start_date = models.DateTimeField('Fecha de inicio', blank=True)
    end_date = models.DateTimeField('Fecha final', blank=True)
    location = models.TextField(verbose_name='Ubicacion', blank=True)
    gmap_link = models.URLField(verbose_name='Link a Google Maps', blank=True, default='', help_text='Link externo de Googlemaps del evento')

    class Meta:
        abstract = True
