from django.contrib import admin
from .models import Subscriber


class SuscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']


admin.site.register(Subscriber, SuscriberAdmin)
