from django.contrib import admin

from .models import Sermon, Tag


class SermonAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created']


admin.site.register(Sermon, SermonAdmin)
admin.site.register(Tag)
