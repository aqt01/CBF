from django.db import models
from CBF.abstract_models import CommonPostInfo
from membership.models import Member

from django.template.defaultfilters import slugify

class Tag(models.Model):
    name = models.CharField('Categoria', max_length=80)

    def __str__(self):
        return self.name

    def get_count_related_objects(self):
        return ( self.sermon_set.count() + self.thought_set.count() + self.event_set.count() )

    def get_related_sermons(self):
        return (self.sermon_set.all())

    def get_related_events(self):
        return (self.event_set.all())

    def get_related_thoughts(self):
        return (self.thought_set.all())


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

    def get_tags(self):
        return (self.tags.all())


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sermon, self).save(*args, **kwargs)
