# Generated by Django 4.2.4 on 2023-08-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]