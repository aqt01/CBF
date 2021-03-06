from django.db import models
from autoslug import AutoSlugField


class Book(models.Model):
    slug = AutoSlugField(populate_from='name', unique_with='name')
    publication_date = models.DateField(verbose_name="fecha de publicacion")
    image = models.ImageField(blank=True, null=True,
                              verbose_name="Imagen de la portada del libro")
    author = models.CharField(blank=True, null=True, max_length=120)
    book_url = models.URLField(verbose_name="Link de venta en Amazon")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
