from django.contrib import admin
from .models import URLShortner

# Register your models here.
class URLShortnerAdmin(admin.ModelAdmin):
    list_display = ('original_url','short_url','created_at','clicks','expires_at','is_expired')
    list_filter = ('created_at','clicks','is_expired')
    search_fields = ('original_url','short_url')

admin.site.register(URLShortner,URLShortnerAdmin)