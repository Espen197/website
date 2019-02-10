from django.contrib import admin
from .models import Stock, Portfolio


class StockAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Info", {"fields": ["ticker", "portfolio", "date"]}),
        ("Price", {"fields": ["price", "volume"]}),
    ]


admin.site.register(Stock, StockAdmin)
admin.site.register(Portfolio)