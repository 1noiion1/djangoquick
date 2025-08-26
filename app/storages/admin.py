from django.contrib import admin

from .models import Storage

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('company', 'address', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('company__name', 'address')
    readonly_fields = ('created_at',)