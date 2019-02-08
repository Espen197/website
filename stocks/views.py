from django.shortcuts import render
from django.views import generic
from .models import Stock, Portfolio


class IndexView(generic.ListView):
    template = "stocks/index.html"

    def get_queryset(self):
        return Portfolio.objects.all()


class PortfolioView(generic.ListView):
    model = Portfolio
    template = "stocks/index.html"  # change later

    def get_queryset(self):
        return Stock.objects.all()


class StockView(generic.DetailView):
    model = Stock
    template = "stocks/detail.html"

