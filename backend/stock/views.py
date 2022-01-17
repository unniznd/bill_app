from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import StockPagination
from .serializers import StockSerializers
from .models import Stock


class StockView(ListAPIView):
    premission_class = (IsAuthenticated,)

    pagination_class = StockPagination
    serializer_class = StockSerializers

    queryset = Stock.objects.all()

    filter_backends = [SearchFilter,OrderingFilter]
    
    ordering_fields = ('itemCode','quantity','price')
    search_fields = (
        '^itemCode',
        '^itemName',
    )

    def get(self,request,c = None):
       
        if c:
            try:
                item = Stock.objects.get(itemCode=int(c))
                itemSerializer = StockSerializers(item,)
                return Response(itemSerializer.data,status=status.HTTP_200_OK)
            
            except:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
        
        items = self.filter_queryset(Stock.objects.get_queryset().order_by('itemCode'))
        results = self.paginate_queryset(items,)
    
        itemSerializer = StockSerializers(results,many=True)
        return self.get_paginated_response(itemSerializer.data)
       
    
    def post(self, request):
        
        addItem = StockSerializers(data=request.data,many=True)
        if(addItem.is_valid()):
            addItem.save()
            return Response({"status":"successful"},status=status.HTTP_201_CREATED)
            
        else:
            return Response({"status":"error","errors":addItem.errors},status=status.HTTP_400_BAD_REQUEST)
    
      

    def patch(self,request,c):
      
        try:
            item = Stock.objects.get(itemCode=int(c))
            print(request.data.pop("itemCode"))
            print(request.data)
            itemUpdate = StockSerializers(item,data=request.data,partial=True)
            print("if")
            if itemUpdate.is_valid():
                itemUpdate.save()
                return Response({"status":"successful"},status=status.HTTP_200_OK)
                    
            else:
                return Response({"status":"error","errors":itemUpdate.errors},status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self,request,c):

        try:
            item = Stock.objects.get(itemCode=int(c))
            item.delete()
            return Response({"status":"successful"},status=status.HTTP_200_OK)
        except:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)

       
