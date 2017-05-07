from django.db import models
from datetime import datetime

class Tags(models.Model):
    name = models.CharField('Categoria',max_length=80)


SOCIAL_MEDIA_NAME = (
    (0, 'Facebook'),
    (1, 'Instagram'),
    (2, 'Twitter'),
)
#TODO: Define what to connect with this model
class Social_media(models.Model):
    name = models.IntegerField('Nombre de la red social',default=0,choices=SOCIAL_MEDIA_NAME)
    url = models.URLField(max_length=200)

ROLES = (
    (0, 'Pastor titular'),
    (1, 'Pastor/a'),
    (2, 'Diacono/a'),
    (3, 'Editor/a'),
)

#TODO: Author should be part of Use model
class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    social_media = models.ManyToManyField(Social_media)
    telephone = models.CharField(max_length=12)
    cellphone = models.CharField(max_length=12)
    img = models.ImageField()
    role = models.IntegerField(default=5,choices=ROLES)

#TODO: This should be an automatic generated model for every uploaded video on youtube
class Preach(models.Model):
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=500, blank=True)
    date = models.DateField()
    published_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tags)
    url = models.URLField(max_length=200)
    img = models.ImageField('Imagen',upload_to='images')

