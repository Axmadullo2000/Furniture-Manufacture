# Generated by Django 3.2.9 on 2021-12-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification_name', models.CharField(max_length=100)),
                ('small_size', models.CharField(max_length=50)),
                ('large_size', models.CharField(max_length=50)),
                ('condition', models.CharField(choices=[('Brand New', 'new'), ('Brand Old', 'old')], max_length=100)),
                ('sku_number', models.IntegerField()),
                ('shipping', models.CharField(choices=[('Shipping worldwide', 'World wide'), ('Shipping around there country', 'Around country'), ('Around city', 'Around our city')], max_length=100)),
                ('warrantly', models.SmallIntegerField()),
                ('delivery_country', models.CharField(choices=[('Alaska', 'alaska'), ('Hawaii', 'Hawaii'), ('California', 'California'), ('Nevada', 'Nevada'), ('Oregon', 'Oregon'), ('Washington', 'Washington'), ('Colorado', 'Colorado'), ('Idaho', 'Idaho'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('New', 'New'), ('Wyoming', 'Wyoming'), ('Arkansas', 'Arkansas'), ('Illinois', 'Illinois'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky')], max_length=100)),
            ],
        ),
    ]
