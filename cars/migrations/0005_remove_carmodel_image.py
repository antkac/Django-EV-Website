# Generated by Django 4.2.16 on 2024-11-27 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='image',
        ),
    ]
