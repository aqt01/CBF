from django.db import models

from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from newsletter.utils import make_activation_code
from .tasks import task_send_email

import os


# TODO: Every youtube upload should generate this
class Subscriber(TimeStampedModel):
    email = models.EmailField(verbose_name=_("Correo"), max_length=150, unique=True)
    is_active = models.BooleanField(verbose_name=_("Email confirmado?"), max_length=150, default=False)
    activation_code = models.CharField(
                                    verbose_name=_('activation code'), max_length=40,
                                    default=make_activation_code
                                    )

    def save(self, **kwargs):
        task_send_email(
            [self.email],
            'Comunidad Biblica De Fe  suscripcion@' + os.environ.get('MAILGUN_SENDER_DOMAIN'),
            _('Suscribirse a Comunidad Biblica De Fe'),
            _('Para inscribirse ingrese a esta direccion'),
        )

        super(Subscriber, self).save(**kwargs)
