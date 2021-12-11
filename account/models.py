from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CharField

from product.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_list')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def percent(self):
        return (self.sub_total() * 2) / 100

    def over_all(self):
        percent = (self.sub_total() * 2) / 100
        overall = percent + (self.sub_total())
        return overall
