from django.contrib import admin

from .models import Sermon, Tag


class SermonAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'date_created', 'summary']


admin.site.register(Sermon, SermonAdmin)
admin.site.register(Tag)
