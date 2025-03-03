# Generated by Django 4.2.16 on 2024-11-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddConstraint(
            model_name='carmodel',
            constraint=models.UniqueConstraint(fields=('make', 'name'), name='unique_car_model_per_make'),
        ),
    ]
