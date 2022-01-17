from django.urls import path

from .views import SaleView, BillView

urlpatterns = [
    path('bill/<int:c>/',BillView.as_view()),
    path('<int:c>/',SaleView.as_view()),
    path('',SaleView.as_view())
]
