from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админка для товаров
    """
    list_display = ('name', 'model', 'release_date',)
    list_filter = ('name', 'release_date',)
