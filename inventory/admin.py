from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'last_updated')
    search_fields = ('name', 'description')
    list_filter = ('last_updated',)
    ordering = ('-last_updated',)