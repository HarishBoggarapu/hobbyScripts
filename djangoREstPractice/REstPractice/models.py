from django.db import models

# Create your models here.


class SportsRoster(models.Model):
    quaterback = models.TextField()
    widereceiver = models.TextField()
    tightend = models.TextField()
    coach = models.TextField()
    cornerback = models.TextField()
