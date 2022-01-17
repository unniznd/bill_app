from django.urls import path

from .views import ExpenseView

urlpatterns = [
    path('<str:u>/',ExpenseView.as_view()),
    path('<str:u>/<int:c>/',ExpenseView.as_view())
]
