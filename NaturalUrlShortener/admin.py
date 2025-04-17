from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)                   # Register ShortURL model for viewing in admin center
class ShortURLAdmin(admin.ModelAdmin):
    pass