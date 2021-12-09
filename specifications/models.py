from django.db import models

# Create your models here.


class Specification(models.Model):
    condition_choices = (
        ('Brand New', 'new'),
        ('Brand Old', 'old'),
    )
    shipping_choices = (
        ('Shipping worldwide', 'World wide'),
        ('Shipping around there country', 'Around country'),
        ('Around city', 'Around our city'),
    )
    delivery_country_choices = (
        ('Alaska', 'alaska'),
        ('Hawaii', 'Hawaii'),
        ('California', 'California'),
        ('Nevada', 'Nevada'),
        ('Oregon', 'Oregon'),
        ('Washington', 'Washington'),
        ('Colorado', 'Colorado'),
        ('Idaho', 'Idaho'),
        ('Montana', 'Montana'),
        ('Nebraska', 'Nebraska'),
        ('New', 'New'),
        ('Wyoming', 'Wyoming'),
        ('Arkansas', 'Arkansas'),
        ('Illinois', 'Illinois'),
        ('Iowa', 'Iowa'),
        ('Kansas', 'Kansas'),
        ('Kentucky', 'Kentucky'),
        ('Fargona', 'Yassaviy kocha'),
    )
    specification_name = models.CharField(max_length=100)
    small_size = models.CharField(max_length=50)
    large_size = models.CharField(max_length=50)
    condition = models.CharField(choices=condition_choices, max_length=100)
    sku_number = models.IntegerField()
    shipping = models.CharField(choices=shipping_choices, max_length=100)
    warrantly = models.SmallIntegerField()
    delivery_country = models.CharField(choices=delivery_country_choices, max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.specification_name
