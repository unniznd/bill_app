from django.urls import path

from .views import StockView

urlpatterns = [
    path('<str:u>/<int:c>/',StockView.as_view()),
    path('<str:u>/',StockView.as_view())
]
