# Generated by Django 5.0.2 on 2024-02-24 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
