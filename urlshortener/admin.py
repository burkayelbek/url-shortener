from re import search
from django.contrib import admin
from urlshortener.models import Shortener


# admin.site.register(Shortener)

@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    search_fields = ('long_url','short_url')
    list_display= ('long_url','short_url')