from django.contrib import admin

from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("itemCode","itemName","quantity","price")
    search_fields = ("itemName__startswith", "itemCode__startswith")
