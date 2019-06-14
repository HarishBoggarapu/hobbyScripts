from django.db import models

# Create your models here.


class Stock(models.Model):
    symbol = models.TextField()
    price = models.TextField()

    def __str__(self):
        return self.symbol
