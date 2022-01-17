from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .filter import AccountFilter
from .serializers import AccountSerializer
from .models import Account
from .pagination import AccountPagination

from stock.models import Stock
from backend.settings import BASE_URL


class AccountView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    pagination_class = AccountPagination
    serializer_class = AccountSerializer
    
    queryset = Account.objects.all()

    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,]
    
    ordering_fields = ('billnumber','date','itemCode','credit')
    
    filterset_class = AccountFilter

    def get(self,request,u,c=None):
        if u == "all":
            account = self.filter_queryset(Account.objects.get_queryset().order_by('-date','-time'))
            results = self.paginate_queryset(account,)
        
            accountSerializer = AccountSerializer(results,many=True)
            return self.get_paginated_response(accountSerializer.data)
        elif u == "bill":
            if c:
                try:
                    account = Account.objects.filter(itemCode=int(c))
                    accountSerializer = AccountSerializer(account,many=True)
                    return Response(accountSerializer.data,status=status.HTTP_200_OK)
                
                except:
                    return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
            account = self.filter_queryset(Account.objects.get_queryset().order_by('-billnumber','-date','-time'))
            results = self.paginate_queryset(account,)
        
            accountSerializer = AccountSerializer(results,many=True)
            return self.get_paginated_response(accountSerializer.data)
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,u):
        if u == 'add':
            account = AccountSerializer(data=request.data,many=True)
  
            if account.is_valid() and self.isItemCodeValid(request):
                if self.updateStock(request):
                    account.save()
                    return Response({"status":"successful"},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","errors":[{"quantity":"Stock update failed"}]},
                                    status=status.HTTP_400_BAD_REQUEST)

            else:
                
                if account.errors:
                    return Response({"status":"error","errors":account.errors},status=status.HTTP_400_BAD_REQUEST)
                
                else:
                    return Response({"status":"error","errors":[{"itemCode":"itemCode doesn't exist"}]},
                                    status=status.HTTP_400_BAD_REQUEST)
           
        else:
            
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,u):
        if u == "delete":
            try:
                account = Account.objects.filter(itemCode=request.data['itemCode'],
                                                 date=request.data['date'],
                                                billnumber=request.data['billnumber'])
                if account:
                    account.delete()
                    return Response({"status":"successful"},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
               
   
    def isItemCodeValid(self,request):
        for stock in request.data:
            if not Stock.objects.filter(itemCode=stock['itemCode']).exists():
                return False
        
        return True

    def updateStock(self,request):
        for i in request.data:
            try:   
                stock = Stock.objects.filter(itemCode=i['itemCode']).first()
                update = stock.quantity - i["quantity"]
                if not update>=0:
                    return False
            except:
                return False
        for i in request.data:
            try:   
                stock = Stock.objects.filter(itemCode=i['itemCode']).first()
                update = stock.quantity - i["quantity"]
                
                json = {"itemCode":i['itemCode'],"quantity":update}
                if requests.patch(BASE_URL+'stock/update/',json=json, 
                                    headers=request.headers).status_code != 200:
                    return False
                
            
            except:
                return False
        
        return True
            
    