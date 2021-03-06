# Generated by Django 4.0.2 on 2022-03-06 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_cart', '0012_product_available_product_colors_product_instock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='cat_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products_cart.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='new_cat', max_length=200),
        ),
    ]
