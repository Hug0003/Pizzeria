# Generated by Django 4.2.4 on 2023-08-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nom',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]
