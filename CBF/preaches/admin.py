from django.contrib import admin

from .models import Preach
from .models import Social_media
from .models import Author

class SocialMediaInLine(admin.TabularInline):
    model = Social_media

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        SocialMediaInLine,
    ]

admin.site.register(Author,AuthorAdmin)
admin.site.register(Social_media)
admin.site.register(Preach)
