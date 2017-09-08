from django.db import models

from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from newsletter.utils import make_activation_code
from django.core.mail import send_mail
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
        send_mail(
            _('Suscribirse a Comunidad Biblica De Fe'),
            _('Para inscribirse ingrese a esta direccion'),
            os.environ.get('MAILGUN_HOST_USER'),
            [self.email],
        )
        super(Subscriber, self).save(**kwargs)
