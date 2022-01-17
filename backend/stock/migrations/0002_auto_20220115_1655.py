# Generated by Django 3.2.9 on 2022-01-15 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]