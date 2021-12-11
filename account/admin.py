from django.contrib import admin

# Register your models here.
from account.models import CartItem, Cart


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('quantity', )


@admin.register(Cart)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
