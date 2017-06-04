from django.db import models

from preaches.models import Author

class Book(models.Model):
    slug = AutoSlugField(populate_from='name', unique_with='name')
    publication_date = models.DateField(verbose_name="fecha de publicacion")
    image = models.ImageField(blank=True, null=True,
                            verbose_name="Imagen de la portada del libro")
    author = models.CharField(blank=True, null=True)
    book_url = models.URLField(verbose_name="Link de venta en Amazon")

    def __str__(self):
        return self.name


