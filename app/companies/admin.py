from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'owner')
    list_filter = ('created_at',)
    search_fields = ('name', 'inn', 'owner___email')
    readonly_fields = ('created_at',)