from django import forms

from .models import TCDSubscription


class TCDSubscriptionForm(forms.ModelForm):
    class Meta:
        model = TCDSubscription
        exclude = ('email',)
