from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
import pandas as pd

from .filter import SaleFilter
from .serializers import SaleSerializer
from .models import Sale
from .pagination import SalePagination


from stock.models import Stock
from backend.settings import BASE_URL
from account.models import Account

class SaleView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    pagination_class = SalePagination
    serializer_class = SaleSerializer
    
    queryset = Sale.objects.all()

    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,]
    
    ordering_fields = ('billnumber','date','itemCode','credit')
    
    filterset_class = SaleFilter

    def get(self,request,c = None):
        if c:
            try:
                account = Sale.objects.filter(itemCode=int(c))
                saleSerializer = SaleSerializer(account,many=True)
                return Response(saleSerializer.data,status=status.HTTP_200_OK)
            
            except:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
       
       
        sale = self.filter_queryset(Sale.objects.get_queryset().order_by('-billnumber','-date','-time'))
        results = self.paginate_queryset(sale,)
        saleSerializer = SaleSerializer(results,many=True)
        return self.get_paginated_response(saleSerializer.data)
    
    def post(self,request,):
        sale = SaleSerializer(data=request.data,many=True)

        if sale.is_valid() and self.isItemCodeValid(request):
            if self.updateStock(request):
                sale.save()
                acc = Account.objects.filter(date=date.today(),reason="Sales").first()
                df = pd.DataFrame(request.data)
                if acc:
                    amount = acc.amount + float(df['total'].sum())
                    json = {"amount":float(amount)}
                    if requests.patch(BASE_URL+'account/change/',
                            json=json,headers=request.headers).status_code == 200:
                        return Response({"status":"successful"},status=status.HTTP_200_OK)
                    else:
                        return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
                
                json = {"amount":float(df['total'].sum()),"reason":"Sales",}
                print("post")
                if requests.post(BASE_URL+'account/change/',
                        json=[json,],headers=request.headers).status_code == 200:
                    return Response({"status":"successful"},status=status.HTTP_200_OK)
                
                else:
                    return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"status":"error","errors":[{"quantity":"Stock update failed"}]},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            
            if sale.errors:
                return Response({"status":"error","errors":sale.errors},status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response({"status":"error","errors":[{"itemCode":"itemCode doesn't exist"}]},
                                status=status.HTTP_400_BAD_REQUEST)
           
    def delete(self,request,u):
        try:
            account = Sale.objects.filter(itemCode=request.data['itemCode'],
                                                date=request.data['date'],
                                            billnumber=request.data['billnumber'])
            if account:
                account.delete()
                return Response({"status":"successful"},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
        except:
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
        
        print("update called")
        for i in request.data:
            try:   
                stock = Stock.objects.filter(itemCode=i['itemCode']).first()
                update = stock.quantity - i["quantity"]
                
                json = {"itemCode":i['itemCode'],"quantity":update}
                if requests.patch(BASE_URL+'stock/'+str(i['itemCode'])+"/",json=json, 
                                    headers=request.headers).status_code != 200:
                    return False
                
            
            except:
                return False
        
        return True
            
class BillView(ListAPIView):
   
    pagination_class = SalePagination
    serializer_class = SaleSerializer
    
    queryset = Sale.objects.all()

    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,]
    
    ordering_fields = ('billnumber','date','itemCode','credit')
    
    filterset_class = SaleFilter

    def get(self,request,c = None):
        if c:
            try:
                account = Sale.objects.filter(billnumber=int(c))
                saleSerializer = SaleSerializer(account,many=True)
                return Response(saleSerializer.data,status=status.HTTP_200_OK)
            
            except:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
       
       
        sale = self.filter_queryset(Sale.objects.get_queryset().order_by('-billnumber','-date','-time'))
        results = self.paginate_queryset(sale,)
        saleSerializer = SaleSerializer(results,many=True)