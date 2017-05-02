from django.db import models


class Tags(models.Model):
    name = models.CharField('Categoria',max_length=80)


class Image(models.Model):
    img = models.ImageField('Imagen',upload_to='image')


SOCIAL_MEDIA_NAME = (
    (0, 'Facebook'),
    (1, 'Instagram'),
    (2, 'Twitter'),
)
#TODO: Define what to connect with this model
class Social_media(models.Model):
    name = models.IntegerField('Nombre de la red social',default=0,choices=SOCIAL_MEDIA_NAME)
    url = models.URLField()

ROLES = (
    (0, 'Pastor titular'),
    (1, 'Pastor'),
    (2, 'Pastora'),
    (3, 'Diacono'),
    (4, 'Diacona'),
    (5, 'Miembro'),
)

#TODO: Author should be part of Use model
class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    social_media = models.ManyToMany(Social_media)
    telephone = models.CharField(max_length=12)
    cellphone = models.CharField(max_length=12)
    img = models.ForeignKey(Image)
    role = models.IntegerField(default=5,choices=ROLES)
#TODO: This should be an automatic generated model for every uploaded video on youtube
class Preach(models.Model):
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=500, blank=True)
    date = models.DateField()
    published_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(Author)
    tags = models.ManyToMany(Tags)
    url = models.UrlField()
    img = models.ImageField(Image)

# Create your models here.
