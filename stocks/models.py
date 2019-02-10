from django.db import models
from django.utils import timezone


class Portfolio(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Stock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    date = models.DateTimeField("Date added", default=timezone.now())

    def __str__(self):
        return self.ticker + ": " + str(self.volume) + " for " + str(self.price) + " NOK per stykk."


