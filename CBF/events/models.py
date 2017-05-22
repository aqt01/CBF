from django.db import models
from datetime import datetime

class Event(models.Model):
    name = models.CharField(verbose_name='Nombre del evento',max_length=60)
    summary = models.CharField(verbose_name='Resumen del evento',max_length=500,blank=True)
    start_date = models.DateTimeField('Fecha de inicio del evento')
    end_date = models.DateTimeField('Fecha final del evento',blank=True)
    img = models.ImageField(verbose_name='Imagen del evento')
    location = models.TextField(verbose_name='Ubicacion del evento')
    gmap_link = models.URLField(verbose_name='Link de Google Maps', blank=True, default='',help_text='Link externo de Googlemaps del evento')
