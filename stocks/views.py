from django.shortcuts import render
from django.views import generic
from .models import Portfolio


class IndexView(generic.ListView):
    template = "stocks/index.html"

    def get_queryset(self):
        return Portfolio.objects.all()


class DetailView(generic.DetailView):
    model = Portfolio
    template = "stocks/detail.html"

