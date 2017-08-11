from django.contrib import admin
from .models import SocialMedia, Member


class SocialMediaInLine(admin.TabularInline):
    model = SocialMedia
    extra = 1


class MemberAdmin(admin.ModelAdmin):
    inlines = [
        SocialMediaInLine,
    ]


admin.site.register(Member, MemberAdmin)
admin.site.register(SocialMedia)
