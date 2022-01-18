from django_filters.filters import DateFromToRangeFilter, CharFilter, BooleanFilter
from django_filters.rest_framework import FilterSet

from .models import Account


class AccountFilter(FilterSet):
    reason = CharFilter(field_name="reason",lookup_expr='icontains')
    date = DateFromToRangeFilter(field_name="date")
    credit  = BooleanFilter(field_name="credit")


    class Meta:
        model = Account
        fields = ( 'reason','date' ,'credit')