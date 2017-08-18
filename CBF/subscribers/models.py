from django.db import models

from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from newsletter.utils import make_activation_code
from django.core.mail import send_mail


# TODO: Every youtube upload should generate this
class Subscriber(TimeStampedModel):
    email = models.EmailField(verbose_name=_("Correo"), max_length=150)
    is_active = models.EmailField(verbose_name=_("Correo"), max_length=150, default=False)
    activation_code = models.CharField(
                                    verbose_name=_('activation code'), max_length=40,
                                    default=make_activation_code
                                    )

    def save(self, **kwargs):
        send_mail(
            _('Suscribirse a Comunidad Biblica De Fe'),
            'Para inscribirse ingrese a esta direccion',
            'sender@sandboxac1eac980b9746a1a0a67f8110554d3c.mailgun.org',
            [self.email],
            fail_silently=False,
        )
        super(Subscriber, self).save(**kwargs)
