from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField('Categoria',max_length=80)

#TODO: Author should be part of Use model
class Author(models.Model):
    ROLES = (
    (0, 'Pastor titular'),
    (1, 'Pastor'),
    (2, 'Pastora'),
    (3, 'Diacono'),
    (4, 'Diacona'),
    (5, 'Editor'),
    (6, 'Editora'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,default=0)
    telephone = models.CharField(verbose_name='Numero de telefono', max_length=12)
    cellphone = models.CharField(verbose_name='Numero de celular', max_length=12)
    img = models.ImageField(verbose_name='Imagen de perfil', help_text='Tamaño sugerido 36x36',upload_to='')
    role = models.IntegerField(verbose_name='Rol',default=5,choices=ROLES)


#TODO: Define what to connect with this model
class Social_media(models.Model):
    SOCIAL_MEDIA_NAME = (
    (0, 'Facebook'),
    (1, 'Instagram'),
    (2, 'Twitter'),
    )

    name = models.IntegerField('Nombre de la red social',default=0,choices=SOCIAL_MEDIA_NAME)
    url = models.URLField(max_length=200)
    author = models.ForeignKey(Author)



#TODO: This should be an automatic generated model for every uploaded video on youtube
class Preach(models.Model):
    title = models.CharField(verbose_name="Titulo de la predica",max_length=60)
    summary = models.TextField(verbose_name="Resumen",max_length=140, blank=True)
    content = models.TextField(verbose_name="Texto",max_length=800, blank=True)
    date_created = models.DateField(verbose_name="Fecha")
    date_published = models.DateField(verbose_name="Fecha de publicacion",default=datetime.now())
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200)
    img = models.ImageField('Imagen',upload_to='images')
    is_published = models.BooleanField(verbose_name="Publicado?",default=True)

