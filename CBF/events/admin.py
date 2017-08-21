from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'start_date', 'end_date', 'location']
    exclude = ('date_created',)


admin.site.register(Event, EventAdmin)
