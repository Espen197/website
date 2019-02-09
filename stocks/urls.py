from django.urls import path
from . import views

app_name = "stocks"

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('<int:portfolio_id>/', views.DetailView.as_view(), name="Detail"),
]