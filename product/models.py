from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from category.models import Category
from specifications.models import Specification


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='photos/product')
    image_2 = models.FileField(upload_to='photos/product')
    image_3 = models.FileField(upload_to='photos/product', blank=True, null=True)
    image_4 = models.FileField(upload_to='photos/product', blank=True, null=True)
    description = models.TextField(max_length=500)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE, null=True, blank=True)

    def get_url(self):
        return reverse('product_info', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
