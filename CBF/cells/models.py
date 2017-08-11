from django.db import models

from CBF.abstract_models import CommonLocationInfo
from membership.models import Member


class Cell(CommonLocationInfo):
    incharge = models.ForeignKey(Member, null=True, blank=True)

    class Meta:
        verbose_name = "Celula"
        verbose_name_plural = "Celulas"
