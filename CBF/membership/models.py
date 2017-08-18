from django.db import models

from model_utils.models import TimeStampedModel
from filer.fields.image import FilerImageField


class Member(TimeStampedModel):
    ROLES = (
            (0, 'Pastor titular'),
            (1, 'Pastor'),
            (2, 'Pastora'),
            (3, 'Diacono'),
            (4, 'Diacona'),
            (5, 'Editor'),
            (6, 'Editora'),
            (7, 'Miembro'),
    )

    name = models.CharField(verbose_name="Nombre", max_length=150)
    email = models.EmailField(verbose_name="Correo electronico", max_length=100)
    telephone = models.CharField(verbose_name='Numero de telefono', max_length=12, blank=True)
    cellphone = models.CharField(verbose_name='Numero de celular', max_length=12, blank=True)
    role = models.IntegerField(verbose_name='Rol', default=5, choices=ROLES, blank=True)
    role_description = models.CharField(verbose_name="Descripcion del rol", max_length=150, blank=True)

    profile_img = FilerImageField(blank=True, null=True,
                                     verbose_name="Imagen de perfil",
                                     help_text="Tamaño sugerido: 50x50")

    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ['-name']

    def __str__(self):
        return str(self.name)

    def get_role(self):
        return str(self.ROLES[self.role][1])


# TODO: Define what to connect with this model
class SocialMedia(TimeStampedModel):

    SOCIAL_MEDIA_NAME = (
                        (0, 'Facebook'),
                        (1, 'Instagram'),
                        (2, 'Twitter'),
    )

    name = models.IntegerField('Nombre de la red social', default=0, choices=SOCIAL_MEDIA_NAME)
    url = models.URLField(verbose_name="Link de la red social", max_length=200)
    author = models.ForeignKey(Member)

    def __str__(self):
        return str(self.SOCIAL_MEDIA_NAME[self.name][1])


    class Meta:
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"
