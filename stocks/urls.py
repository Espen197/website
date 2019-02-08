from django.urls import path
from . import views

app_name = "stocks"

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('#', views.PortfolioView.as_view(), name="Portfolio"),
    path('#', views.StockView.as_view(), name="Stock"),
]