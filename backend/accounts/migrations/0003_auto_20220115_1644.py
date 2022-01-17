# Generated by Django 3.2.9 on 2022-01-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_accounts_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='discount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]