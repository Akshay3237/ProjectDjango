
from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_id', 'subject', 'semester')
    list_filter = ('subject', 'semester')
    search_fields = ('subject__subject_name',)