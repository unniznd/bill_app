# Generated by Django 3.2.9 on 2022-01-16 07:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='discount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='quantity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='total',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
