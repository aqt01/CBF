from django.db import models
from sermons.models import Tag
from CBF.abstract_models import CommonLocationInfo


class Event(CommonLocationInfo):
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


