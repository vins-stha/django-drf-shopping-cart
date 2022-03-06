# Generated by Django 4.0.2 on 2022-03-06 16:53

from django.db import migrations, models
import products_cart.models


class Migration(migrations.Migration):

    dependencies = [
        ('products_cart', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='empty_cart.png', upload_to=products_cart.models.upload_to, verbose_name='Product-image'),
        ),
    ]
