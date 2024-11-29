# Generated by Django 5.1.3 on 2024-11-22 20:54

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Other', max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acceleration', models.FloatField(help_text='Acceleration in seconds (0-100 km/h)')),
                ('top_speed', models.FloatField(help_text='Top speed in km/h')),
                ('drive', models.CharField(help_text='e.g., RWD, FWD, AWD', max_length=20)),
                ('battery', models.FloatField(help_text='Usable battery capacity in kWh')),
                ('charge_power', models.FloatField(help_text='Maximum charge power in kW')),
                ('real_range', models.IntegerField(help_text='Real-world range in km')),
                ('efficiency', models.IntegerField(help_text='Efficiency in Wh/km')),
                ('seats', models.IntegerField(help_text='Number of seats', validators=[django.core.validators.MinValueValidator(1)])),
                ('tow_hitch', models.BooleanField(default=False, help_text='Tow hitch available?')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.carmake')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('is_available', models.BooleanField(default=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('is_active', models.BooleanField(default=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='cars.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='cars.customer')),
            ],
        ),
    ]
