from functools import partial
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from datetime import date

from .filter import AccountFilter
from .pagination import AccountPagination
from .models import Account
from .serializers import AccountSerializer
from .algo import income, expense

class AccountView(ListAPIView):

    #permission_classes = (IsAuthenticated,)

    serializer_class = AccountSerializer
    pagination_class = AccountPagination

    queryset = Account.objects.all()

    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,]

    ordering_fields = ('date','credit')
    
    filterset_class = AccountFilter

    def get(self,request):
            account = self.filter_queryset(Account.objects.get_queryset().order_by('-date','-time'))
            results = self.paginate_queryset(account,)
        
            accountSerializer = AccountSerializer(results,many=True)
            return self.get_paginated_response(accountSerializer.data)

    def post(self,request,):
    
        expense = AccountSerializer(data=request.data,many=True)
        if expense.is_valid():
            expense.save()
            return Response({"status":"successful"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request):
        try:
            expense = Account.objects.filter(billnumber=request.data['billnumber'],
                                            date=request.data['date'],
                                            reason=request.data['reason'])
            if expense:
                expense.delete()
                return Response({"status":"successful"},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        acc = Account.objects.filter(date=date.today(),reason="Sales").first()
        expense = AccountSerializer(acc,data=request.data,partial = True)
        if expense.is_valid():
            expense.save()
            return Response({"status":"successful"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
      

class AccountReportView(ListAPIView):
    def get(self,request):
        json = {
            "income":income(),
            "expense":expense(),
            "inHand":income()- expense()
        }
        return Response(json, status=status.HTTP_200_OK)