# Generated by Django 3.2.9 on 2022-01-17 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billnumber', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('itemCode', models.IntegerField()),
                ('itemName', models.CharField(max_length=1000)),
                ('quantity', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('discount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('total', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('time', models.TimeField(auto_now_add=True)),
                ('credit', models.BooleanField(default=False)),
            ],
        ),
    ]
