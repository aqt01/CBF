from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task


@shared_task(bind=True)
def task_send_email(self, recipe_to, recipe_from, recipe_subject, message):
    send_mail(
        recipe_subject,
        message,
        recipe_from,
        recipe_to,
        fail_silently=False,
    )
