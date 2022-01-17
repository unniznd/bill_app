from django.urls import path

from .views import SaleView

urlpatterns = [
    path('<str:u>/',SaleView.as_view()),
    path('<str:u>/<int:c>/',SaleView.as_view())
]
