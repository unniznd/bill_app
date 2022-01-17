from django.db import models
from django.core.validators import MinValueValidator

class Stock(models.Model):
    itemCode = models.IntegerField(unique=True)
    itemName = models.CharField(max_length=1000)
    quantity = models.FloatField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0)])





