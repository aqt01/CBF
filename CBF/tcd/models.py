import uuid

from django.db import models

from model_utils.models import TimeStampedModel
from filer.fields.file import FilerFileField


class TCDSubscription(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(blank=True, null=True, verbose_name="Nombre", max_length=150, unique=True)
    last_name = models.CharField(blank=True, null=True, verbose_name="Apellidos", max_length=150, unique=True)
    email = models.EmailField(max_length=100, verbose_name='Correo electrónico') # should add a reference to newsletter
    cellphone = models.CharField(blank=True, null=True, max_length=15)
    voucher = FilerFileField(blank=True, null=True,
                          verbose_name="voucher",
                          help_text="Tamaño sugerido: 1024x765")

    class Meta:
        verbose_name = "Subscriptor"
        verbose_name_plural = "Subscriptors"
