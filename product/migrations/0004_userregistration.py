# Generated by Django 3.2.9 on 2021-11-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
