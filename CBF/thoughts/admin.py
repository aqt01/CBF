from django.contrib import admin

from .models import Thought


class ThoughtAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'summary', 'date_created']


admin.site.register(Thought, ThoughtAdmin)
