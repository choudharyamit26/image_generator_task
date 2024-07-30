from django.contrib import admin

from .models import GeneratedImage


@admin.register(GeneratedImage)
class GeneratedImageAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'image','file_path')
    search_fields = ('prompt',)
