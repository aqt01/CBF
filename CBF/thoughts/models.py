from django.db import models
from CBF.abstract_models import CommonPostInfo
from sermons.models import Member, Tag

# Create your models here.


class Thought(CommonPostInfo):
    author = models.ForeignKey(Member, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Reflexion"
        verbose_name_plural = "Reflexiones"
