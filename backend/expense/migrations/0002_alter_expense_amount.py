# Generated by Django 3.2.9 on 2022-01-16 07:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]