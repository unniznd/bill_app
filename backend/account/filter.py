from django_filters.filters import DateFromToRangeFilter, NumberFilter, BooleanFilter
from django_filters.rest_framework import FilterSet

from .models import Account


class AccountFilter(FilterSet):
    date = DateFromToRangeFilter(field_name="date")
    credit  = BooleanFilter(field_name="credit")


    class Meta:
        model = Account
        fields = ( 'date' ,'credit')