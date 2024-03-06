from django.contrib import admin
from .models import Spot

@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name', 'description']

