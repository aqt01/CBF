from django.db import models
from CBF.abstract_models import CommonPostInfo
from membership.models import Member


class Tag(models.Model):
    name = models.CharField('Categoria', max_length=80)

    def __str__(self):
        return self.name


# TODO: Every youtube upload should generate this
class Sermon(CommonPostInfo):
    url = models.URLField(max_length=250)
    author = models.ForeignKey(Member, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = "Sermon"
        verbose_name_plural = "Sermones"

    def __str__(self):
        return self.name
