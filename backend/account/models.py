from django.db import models

from django.core.validators import MinValueValidator

class Account(models.Model):
    date = models.DateField(auto_now_add=True)
    reason = models.CharField(max_length=200)
    amount = models.FloatField(validators=[MinValueValidator(0)])
    time = models.TimeField(auto_now_add=True)
    credit = models.BooleanField(default=False)
