from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .filter import ExpenseFilter
from .pagination import ExpensePagination
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseView(ListAPIView):

    permission_classes = (IsAuthenticated,)

    serializer_class = ExpenseSerializer
    pagination_class = ExpensePagination

    queryset = Expense.objects.all()

    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,]

    ordering_fields = ('billnumber','date','credit')
    
    filterset_class = ExpenseFilter

    def get(self,request,u,c = None):
        if u == "all":
            expense = self.filter_queryset(Expense.objects.get_queryset().order_by('-date','-time'))
            results = self.paginate_queryset(expense,)
        
            expenseSerializer = ExpenseSerializer(results,many=True)
            return self.get_paginated_response(expenseSerializer.data)
        elif u == "bill":
            if c:
                try:
                    expense = Expense.objects.filter(itemCode=int(c))
                    expenseSerializer = ExpenseSerializer(expense,many=True)
                    return Response(expenseSerializer.data,status=status.HTTP_200_OK)
                
                except:
                    return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
            account = self.filter_queryset(Expense.objects.get_queryset().order_by('-billnumber','-date','-time'))
            results = self.paginate_queryset(account,)
        
            expenseSerializer = ExpenseSerializer(results,many=True)
            return self.get_paginated_response(expenseSerializer.data)
        else:
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,u):
        if u == 'add':
            expense = ExpenseSerializer(data=request.data,many=True)
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

