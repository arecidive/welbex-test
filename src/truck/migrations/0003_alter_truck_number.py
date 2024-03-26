# Generated by Django 5.0.3 on 2024-03-26 11:12

import truck.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0002_alter_truck_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='number',
            field=models.CharField(max_length=5, unique=True, validators=[truck.validators.validate_truck_number], verbose_name='Номер машины'),
        ),
    ]