from django.db import models

from django.core.validators import MinValueValidator

class Account(models.Model):
    billnumber = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    itemCode = models.IntegerField()
    itemName = models.CharField(max_length=1000)
    quantity = models.FloatField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0)])
    amount = models.FloatField(validators=[MinValueValidator(0)])
    discount = models.FloatField(validators=[MinValueValidator(0)])
    total = models.FloatField(validators=[MinValueValidator(0)])
    time = models.TimeField(auto_now_add=True)
    credit = models.BooleanField(default=False)