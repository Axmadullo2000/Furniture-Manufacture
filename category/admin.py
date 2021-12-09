from django.contrib import admin

# Register your models here.
from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'description', 'image')
    prepopulated_fields = {'slug': ('category_name', )}
