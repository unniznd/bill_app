from django_filters.filters import DateFromToRangeFilter, NumberFilter, BooleanFilter
from django_filters.rest_framework import FilterSet

from .models import Expense


class ExpenseFilter(FilterSet):
    billnumber = NumberFilter(field_name="billnumber")
    date = DateFromToRangeFilter(field_name="date")
    credit  = BooleanFilter(field_name="credit")


    class Meta:
        model = Expense
        fields = ('billnumber', 'date' ,'credit')