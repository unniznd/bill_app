from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("billnumber","date","reason","amount","time","credit",)
    search_fields = ("billnumber__startswith", "reason__startswith")
    list_filter = ('billnumber','date','credit',)