from django.db import models
from expenses import ml_model

class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
