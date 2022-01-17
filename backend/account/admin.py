from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("date","reason","amount","time","credit",)
    search_fields = ( "reason__startswith","date__startswith")
    list_filter = ('date','credit',)