from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.FileField(upload_to='photos/category')

    class Meta:
        verbose_name = 'categorie'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
