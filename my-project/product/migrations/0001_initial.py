# Generated by Django 5.0.2 on 2024-02-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
            ],
        ),
    ]