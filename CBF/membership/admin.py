from django.contrib import admin
from .models import SocialMedia, Member


class SocialMediaInLine(admin.TabularInline):
    model = SocialMedia
    extra = 1


class MemberAdmin(admin.ModelAdmin):
    inlines = [
        SocialMediaInLine,
    ]
    list_display = ['name', 'email', 'role_description']


admin.site.register(Member, MemberAdmin)
admin.site.register(SocialMedia)
