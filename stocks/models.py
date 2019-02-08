from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    opening = models.DecimalField(max_digits=10, decimal_places=3)
    close = models.DecimalField(max_digits=10, decimal_places=3)
    volume = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return self.ticker + ": " + self.price


class Portfolio(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    percentage_of_portfolio = models.DecimalField(max_digits=7, decimal_places=3)
