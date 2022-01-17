from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .filter import AccountFilter
from .pagination import AccountPagination
from .models import Account
from .serializers import AccountSerializer

class AccountView(ListAPIView):

    #permission_classes = (IsAuthenticated,)

    serializer_class = AccountSerializer
    pagination_class = AccountPagination

    queryset = Account.objects.all()

    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,]

    ordering_fields = ('date','credit')
    
    filterset_class = AccountFilter

    def get(self,request,u,c = None):
        if u == "all":
            account = self.filter_queryset(Account.objects.get_queryset().order_by('-date','-time'))
            results = self.paginate_queryset(account,)
        
            accountSerializer = AccountSerializer(results,many=True)
            return self.get_paginated_response(accountSerializer.data)
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,u):
        if u == 'add':
            expense = AccountSerializer(data=request.data,many=True)
            if expense.is_valid():
                expense.save()
                return Response({"status":"successful"},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,u):
        if u == "delete":
            try:
                expense = Expense.objects.filter(billnumber=request.data['billnumber'],
                                                date=request.data['date'],
                                                reason=request.data['reason'])
                if expense:
                    expense.delete()
                    return Response({"status":"successful"},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)

