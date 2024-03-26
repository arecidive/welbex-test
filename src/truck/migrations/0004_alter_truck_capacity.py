# Generated by Django 5.0.3 on 2024-03-26 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0003_alter_truck_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='capacity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Грузоподъемность должна быть не меньше 1!'), django.core.validators.MaxValueValidator(1000, message='Грузоподъемность должна быть не больше 1000!')], verbose_name='Грузоподъемность'),
        ),
    ]
