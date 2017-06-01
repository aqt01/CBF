from django.db import models

from preaches.models import Author
from preaches.models import Tag
# Create your models here.

class Message(models.Model):
    name = models.CharField(verbose_name="Nombre",max_length=150)
    summary = models.CharField(verbose_name="Resumen",max_length=140)
    message = models.TextField(verbose_name="Contenido",max_length=1200)
    author = models.ForeignKey(Author)
    date_created = models.DateTimeField(verbose_name="Fecha de creacion",auto_now_add=True, blank=True)
    date_published = models.DateTimeField(verbose_name="Fecha de publicacion",auto_now_add=True)
    is_published = models.BooleanField(verbose_name="Publicado?",default=True)
    tags = models.ManyToManyField(Tag)
