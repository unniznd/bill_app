from django_filters.filters import DateFromToRangeFilter, NumberFilter, BooleanFilter
from django_filters.rest_framework import FilterSet

from .models import Account


class AccountFilter(FilterSet):
    billnumber = NumberFilter(field_name="billnumber")
    itemCode = NumberFilter(field_name="itemCode")
    date = DateFromToRangeFilter(field_name="date")
    credit  = BooleanFilter(field_name="credit")
    income = BooleanFilter(field_name="income")


    class Meta:
        model = Account
        fields = ('billnumber', 'date','itemCode','credit')