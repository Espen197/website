from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Stock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    # opening = models.DecimalField(max_digits=10, decimal_places=3)
    # close = models.DecimalField(max_digits=10, decimal_places=3)
    volume = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return self.ticker + ": " + self.price


