# Generated by Django 5.1 on 2024-08-26 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_image_product_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggregate',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aggregates', to='product.product'),
        ),
    ]
