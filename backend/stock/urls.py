from django.urls import path

from .views import StockView

urlpatterns = [

    path('<int:c>/',StockView.as_view()),
    path('',StockView.as_view())
]
