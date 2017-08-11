from django.contrib import admin

from .models import Sermon, Tag


admin.site.register(Sermon)
admin.site.register(Tag)
