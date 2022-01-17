from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("billnumber","date","itemCode","itemName",
                    "quantity","price","amount","discount","total","time","credit",)
    search_fields = ("itemName__startswith", "itemCode__startswith")
    list_filter = ('billnumber','date','itemCode','itemName','credit',)