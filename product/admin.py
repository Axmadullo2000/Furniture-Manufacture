from django.contrib import admin
# Register your models here.
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'image', 'image_2', 'description')
    prepopulated_fields = {'slug': ('product_name', )}

